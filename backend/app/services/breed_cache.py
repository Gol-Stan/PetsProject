import json
from app.redis_client import redis_client
from app.config import settings

class BreedCache:

    def __init__(self):
        self.redis = redis_client
        self.breed_key = "breeds:all"
        self.breed_key_prefix = "breed:"
        self.cache = 3600

    async def get_all_breeds(self):
        try:
            cached_data = await self.redis.get(self.breed_key)
            if cached_data:
                return json.loads(cached_data)
            return None
        except Exception as e:
            print(f"Redis error in all_breeds: {e}")
            return None

    async def set_all_breeds(self, breeds_data):
        try:
            await self.redis.setex(
                self.breed_key,
                self.cache,
                json.dumps(breeds_data, default=str)
            )
        except Exception as e:
            print(f"Redis error in set_breeds: {e}")

    async def get_breed_by_id(self, breed_id: int):
        try:
            cached_data = await self.redis.get(f"{self.breed_key_prefix}{breed_id}")
            if cached_data:
                return json.loads(cached_data)
            return None
        except Exception as e:
            print(f"Redis error breed_id: {e}")
            return None

    async def set_breed(self, breed_id: int, breed_data):
        try:
            await self.redis.setex(
                f"{self.breed_key_prefix}{breed_id}",
                self.cache,
                json.dumps(breed_data, default=str)
            )
        except Exception as e:
            print(f"Redis set_breed: {e}")

    async def invalidate_all_breeds(self):
        try:
            await self.redis.delete(self.breed_key)

            keys = await self.redis.keys(f"{self.breed_key_prefix}")
            if keys:
                await self.redis.delete(*keys)

            print("Cache invalidated")
        except Exception as e:
            print(f"Redis breeds invalidate error: {e}")

    async def invalidate_breed(self, breed_id: int):
        try:
            await self.redis.delete(f"{self.breed_key_prefix}{breed_id}")
        except Exception as e:
            print(f"Redis breed invalidte error: {e}")


breed_cache = BreedCache()