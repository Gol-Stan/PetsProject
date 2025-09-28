from fastapi import FastAPI, Depends
from sqlalchemy.engine.reflection import cache
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import models, config

from app.celery_worker import add
from app.redis_client import redis_client
import time

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@app.get("/db-info")
def db_info():
    return {
        "database_url": config.settings.DATABASE_URL,
        "db-user": config.settings.POSTGRES_USER
    }

@app.get("/add")
def call_add(x:int, y:int):
    task = add.delay(x, y)
    return {"task_id": task.id, "status": "started"}

@app.get("/expensive-data/{item_id}")
def get_expensive_data(item_id: int):
    cache_key = f"item:{item_id}"
    cached = redis_client.get(cache_key)
    if cached:
        return {"item_id": item_id, "data_cached": cached, "source": "cache"}

    time.sleep(2)
    data = f"Data for item {item_id}"
    redis_client.setex(cache_key, 60, data)
    return {"item_id": item_id, "data_cached": data, "source": "server"}