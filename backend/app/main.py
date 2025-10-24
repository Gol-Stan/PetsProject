from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.staticfiles import StaticFiles

from app.database import get_db
from app import models, config
from app.routers import user, pet, breed
from app.celery_worker import add
from app.redis_client import redis_client
import asyncio

app = FastAPI()

app.include_router(user.router, prefix="/auth")
app.include_router(pet.router, prefix="/pets")
app.include_router(breed.router, prefix="/breeds")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/")
async def read_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(models.User))
    users = result.scalars().all()
    return users


@app.get("/db-info")
async def db_info():
    return {
        "database_url": config.settings.DATABASE_URL,
        "db-user": config.settings.POSTGRES_USER
    }

@app.get("/add")
async def call_add(x:int, y:int):
    task = add.delay(x, y)
    return {"task_id": task.id, "status": "started"}

@app.get("/expensive-data/{item_id}")
async def get_expensive_data(item_id: int):
    cache_key = f"item:{item_id}"
    cached = await redis_client.get(cache_key)
    if cached:
        return {"item_id": item_id, "data_cached": cached, "source": "cache"}

    await asyncio.sleep(2)
    data = f"Data for item {item_id}"
    await redis_client.setex(cache_key, 60, data)
    return {"item_id": item_id, "data_cached": data, "source": "server"}