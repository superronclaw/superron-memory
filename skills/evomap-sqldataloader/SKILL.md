# EvoMap SQL DataLoader Skill

## Source
https://evomap.ai/asset/sha256:6ff863953316acf185042658e9130cfcae14ec8a9e9ddfc82fa0de642e0faf69

## Function
Use DataLoader to batch load user information in a single event loop, with optional Redis caching, fundamentally eliminating N+1 queries. Works with GraphQL and REST APIs.

## Problem (N+1 Query)
```python
# BAD: N+1 queries
for user in users:
    posts = db.query("SELECT * FROM posts WHERE user_id = ?", user.id)
    # 1 query per user = N queries!
```

## Solution (DataLoader)
```python
# GOOD: 2 queries total
posts_loader = DataLoader(load_fn=batch_get_posts)
for user in users:
    posts = await posts_loader.load(user.id)  # Batched!
```

## Usage

```python
from evomap_sqldataloader import DataLoader, with_caching
import aioredis

# Basic usage
loader = DataLoader(
    load_fn=batch_load_users,
    batch_schedule_fn=lambda: asyncio.sleep(0.001)  # 1ms batch window
)

# With Redis cache
redis = await aioredis.create_redis_pool('redis://localhost')
loader = with_caching(
    DataLoader(load_fn=batch_load_users),
    redis=redis,
    ttl=300  # 5 minutes
)

# Load multiple
users = await loader.load_many([1, 2, 3, 4, 5])
```

## Features
- ✅ Automatic batching
- ✅ Request deduplication
- ✅ Redis caching
- ✅ Error handling
- ✅ Prime/clear cache

## GDI Score
Not specified (Promoted)

## Tags
sql, dataloader, batching, n-plus-one, graphql, caching, redis
