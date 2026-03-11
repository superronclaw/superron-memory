import asyncio
import logging
from typing import Callable, List, Any, Optional, Dict, Set, TypeVar, Generic
from dataclasses import dataclass
from collections import defaultdict
import time

logger = logging.getLogger(__name__)

T = TypeVar('T')
K = TypeVar('K')

@dataclass
class LoadResult(Generic[T]):
    """Result of a batch load operation."""
    key: Any
    value: Optional[T] = None
    error: Optional[Exception] = None
    
    def get(self) -> T:
        """Get value or raise error."""
        if self.error:
            raise self.error
        return self.value


class DataLoader(Generic[K, T]):
    """
    DataLoader for batching and caching data fetches.
    Eliminates N+1 query problem.
    """
    
    def __init__(
        self,
        load_fn: Callable[[List[K]], asyncio.Future[List[T]]],
        batch_schedule_fn: Optional[Callable[[], asyncio.Future]] = None,
        cache_map: Optional[Dict[K, asyncio.Future]] = None,
        max_batch_size: Optional[int] = None
    ):
        self._load_fn = load_fn
        self._batch_schedule_fn = batch_schedule_fn or self._default_schedule
        self._cache = cache_map if cache_map is not None else {}
        self._max_batch_size = max_batch_size or 1000
        
        self._queue: List[K] = []
        self._futures: Dict[K, asyncio.Future] = {}
        self._dispatch_scheduled = False
        self._lock = asyncio.Lock()
        
    @staticmethod
    async def _default_schedule():
        """Default batch scheduling - process on next event loop tick."""
        await asyncio.sleep(0)
    
    async def load(self, key: K) -> T:
        """Load a single item by key."""
        # Check cache
        if key in self._cache:
            return await self._cache[key]
        
        # Check if already queued
        if key in self._futures:
            return await self._futures[key]
        
        # Create future and queue
        future = asyncio.get_event_loop().create_future()
        self._futures[key] = future
        self._queue.append(key)
        
        # Schedule dispatch if not already scheduled
        if not self._dispatch_scheduled:
            self._dispatch_scheduled = True
            asyncio.create_task(self._dispatch_after_schedule())
        
        return await future
    
    async def load_many(self, keys: List[K]) -> List[T]:
        """Load multiple items by keys."""
        return await asyncio.gather(*[self.load(key) for key in keys])
    
    async def _dispatch_after_schedule(self):
        """Wait for schedule then dispatch batch."""
        await self._batch_schedule_fn()
        await self._dispatch()
    
    async def _dispatch(self):
        """Dispatch the batch load."""
        async with self._lock:
            if not self._queue:
                self._dispatch_scheduled = False
                return
            
            # Take current queue
            keys = self._queue[:self._max_batch_size]
            futures = {k: self._futures[k] for k in keys}
            
            self._queue = self._queue[self._max_batch_size:]
            self._futures = {}
            
            # Schedule next batch if needed
            if self._queue:
                self._dispatch_scheduled = True
                asyncio.create_task(self._dispatch_after_schedule())
            else:
                self._dispatch_scheduled = False
        
        # Execute batch load (outside lock)
        try:
            values = await self._load_fn(keys)
            
            # Resolve futures
            for i, key in enumerate(keys):
                if key in futures:
                    if i < len(values):
                        futures[key].set_result(values[i])
                    else:
                        futures[key].set_exception(
                            IndexError(f"No value returned for key {key}")
                        )
        except Exception as e:
            # Reject all futures on error
            for future in futures.values():
                future.set_exception(e)
    
    def prime(self, key: K, value: T):
        """Prime the cache with a value."""
        future = asyncio.get_event_loop().create_future()
        future.set_result(value)
        self._cache[key] = future
    
    def clear(self, key: Optional[K] = None):
        """Clear cache for a key or all keys."""
        if key is not None:
            self._cache.pop(key, None)
        else:
            self._cache.clear()
    
    def clear_all(self):
        """Clear entire cache."""
        self._cache.clear()


class CachedDataLoader(DataLoader):
    """DataLoader with Redis caching support."""
    
    def __init__(
        self,
        load_fn: Callable[[List[K]], asyncio.Future[List[T]]],
        redis_client=None,
        cache_key_fn: Optional[Callable[[K], str]] = None,
        ttl: int = 300,
        **kwargs
    ):
        super().__init__(load_fn, **kwargs)
        self._redis = redis_client
        self._cache_key_fn = cache_key_fn or (lambda k: f"dataloader:{k}")
        self._ttl = ttl
    
    async def load(self, key: K) -> T:
        """Load with Redis cache check."""
        if self._redis:
            cache_key = self._cache_key_fn(key)
            cached = await self._redis.get(cache_key)
            if cached:
                import json
                return json.loads(cached)
        
        return await super().load(key)
    
    async def _dispatch(self):
        """Dispatch and cache results."""
        async with self._lock:
            if not self._queue:
                self._dispatch_scheduled = False
                return
            
            keys = self._queue[:self._max_batch_size]
            futures = {k: self._futures[k] for k in keys}
            
            self._queue = self._queue[self._max_batch_size:]
            self._futures = {}
            
            if self._queue:
                self._dispatch_scheduled = True
                asyncio.create_task(self._dispatch_after_schedule())
            else:
                self._dispatch_scheduled = False
        
        try:
            values = await self._load_fn(keys)
            
            # Cache to Redis if available
            if self._redis:
                import json
                pipe = self._redis.pipeline()
                for i, key in enumerate(keys):
                    if i < len(values):
                        cache_key = self._cache_key_fn(key)
                        pipe.setex(
                            cache_key,
                            self._ttl,
                            json.dumps(values[i])
                        )
                await pipe.execute()
            
            # Resolve futures
            for i, key in enumerate(keys):
                if key in futures:
                    if i < len(values):
                        futures[key].set_result(values[i])
                    else:
                        futures[key].set_exception(
                            IndexError(f"No value returned for key {key}")
                        )
        except Exception as e:
            for future in futures.values():
                future.set_exception(e)


# Utility functions
def with_caching(loader_class=DataLoader):
    """Decorator to add caching to a DataLoader."""
    def decorator(redis_client=None, ttl=300):
        def wrapper(load_fn):
            return CachedDataLoader(
                load_fn=load_fn,
                redis_client=redis_client,
                ttl=ttl
            )
        return wrapper
    return decorator


# Example usage
if __name__ == "__main__":
    async def example():
        """Example DataLoader usage."""
        
        # Simulate database
        db = {
            1: {"id": 1, "name": "Alice"},
            2: {"id": 2, "name": "Bob"},
            3: {"id": 3, "name": "Charlie"},
        }
        
        async def batch_load_users(ids: List[int]) -> List[dict]:
            """Batch load users from database."""
            print(f"Batch loading users: {ids}")  # Called once!
            await asyncio.sleep(0.1)  # Simulate DB latency
            return [db.get(id) for id in ids]
        
        # Create loader
        loader = DataLoader(load_fn=batch_load_users)
        
        # Load multiple users - only one batch query!
        users = await loader.load_many([1, 2, 3])
        print(f"Loaded: {users}")
        
        # Load again - cached
        user = await loader.load(1)
        print(f"Cached: {user}")
    
    asyncio.run(example())
