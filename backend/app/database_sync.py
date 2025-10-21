from sqlalchemy import create_engine
from app.config import settings
from app.database import Base

DATABASE_URL_SYNC = settings.db_url.replace("asyncpg", "psycopg2")
engine_sync = create_engine(DATABASE_URL_SYNC)