from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import models, config

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