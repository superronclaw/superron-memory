import asyncio
import logging
from typing import Optional, Any, Dict
from dataclasses import dataclass, field
from contextlib import asynccontextmanager
import aiohttp
import time

logger = logging.getLogger(__name__)

@dataclass
class ThrottleStats:
    """Statistics for throttled operations."""
    total_requests: int = 0
    active_requests: int = 0
    queued_requests: int = 0
    completed_requests: int = 0
    failed_requests: int = 0
    avg_wait_time: float = 0.0
    
class AsyncIOThrottle:
    """
    AsyncIO semaphore-based throttling for connection pooling.
    Prevents resource exhaustion under high concurrency.
    """
    
    def __init__(
        self,
        max_concurrent: int = 10,
        name: str = "default"
    ):
        self.max_concurrent = max_concurrent
        self.name = name
        self._semaphore = asyncio.Semaphore(max_concurrent)
        self._stats = ThrottleStats()
        self._lock = asyncio.Lock()
        
    @asynccontextmanager
    async def acquire(self, timeout: Optional[float] = None):
        """Acquire semaphore with optional timeout."""
        start_time = time.time()
        async with self._lock:
            self._stats.queued_requests += 1
        
        try:
            if timeout:
                acquired = await asyncio.wait_for(
                    self._semaphore.acquire(),
                    timeout=timeout
                )
            else:
                await self._semaphore.acquire()
                acquired = True
            
            if acquired:
                wait_time = time.time() - start_time
                async with self._lock:
                    self._stats.queued_requests -= 1
                    self._stats.active_requests += 1
                    self._stats.total_requests += 1
                    # Update rolling average
                    n = self._stats.completed_requests + self._stats.active_requests
                    self._stats.avg_wait_time = (
                        (self._stats.avg_wait_time * (n - 1) + wait_time) / n
                    )
                
                try:
                    yield self
                finally:
                    async with self._lock:
                        self._stats.active_requests -= 1
                        self._stats.completed_requests += 1
                    self._semaphore.release()
        except asyncio.TimeoutError:
            async with self._lock:
                self._stats.queued_requests -= 1
                self._stats.failed_requests += 1
            raise
    
    async def __aenter__(self):
        await self._semaphore.acquire()
        async with self._lock:
            self._stats.active_requests += 1
            self._stats.total_requests += 1
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        async with self._lock:
            self._stats.active_requests -= 1
            if exc_type is None:
                self._stats.completed_requests += 1
            else:
                self._stats.failed_requests += 1
        self._semaphore.release()
        return False
    
    def get_stats(self) -> Dict[str, Any]:
        """Get current statistics."""
        return {
            "name": self.name,
            "max_concurrent": self.max_concurrent,
            "total_requests": self._stats.total_requests,
            "active_requests": self._stats.active_requests,
            "queued_requests": self._stats.queued_requests,
            "completed_requests": self._stats.completed_requests,
            "failed_requests": self._stats.failed_requests,
            "avg_wait_time_ms": round(self._stats.avg_wait_time * 1000, 2)
        }
    
    def update_limit(self, new_limit: int):
        """Dynamically update concurrency limit."""
        diff = new_limit - self.max_concurrent
        if diff > 0:
            # Increase: release more slots
            for _ in range(diff):
                self._semaphore.release()
        self.max_concurrent = new_limit
        logger.info(f"Updated concurrency limit to {new_limit}")


class ThrottledClient:
    """HTTP client with throttling support."""
    
    def __init__(
        self,
        max_concurrent: int = 10,
        session: Optional[aiohttp.ClientSession] = None
    ):
        self.throttle = AsyncIOThrottle(max_concurrent)
        self._session = session or aiohttp.ClientSession()
        self._owned_session = session is None
        
    async def request(
        self,
        method: str,
        url: str,
        **kwargs
    ) -> aiohttp.ClientResponse:
        """Make throttled HTTP request."""
        async with self.throttle:
            return await self._session.request(method, url, **kwargs)
    
    async def get(self, url: str, **kwargs) -> aiohttp.ClientResponse:
        return await self.request("GET", url, **kwargs)
    
    async def post(self, url: str, **kwargs) -> aiohttp.ClientResponse:
        return await self.request("POST", url, **kwargs)
    
    async def close(self):
        """Close client session."""
        if self._owned_session:
            await self._session.close()
    
    def get_stats(self) -> Dict[str, Any]:
        return self.throttle.get_stats()
