import redis.asyncio as redis
import os


"""REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0)) """

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

#redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)
redis_client = redis.from_url(REDIS_URL, decode_response=True)

async def check_redis():
    try:
        pong = await redis_client.ping()
        if pong:
            print("Redis connected")
    except Exception:
        print("Connection error")
