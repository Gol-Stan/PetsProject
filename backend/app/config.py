import os
from dotenv import load_dotenv
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    POSTGRES_USER: str = "dev_user"
    POSTGRES_PASSWORD: str = "dev_password"
    POSTGRES_DB: str = "dev_db"
    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5432
    DATABASE_URL: str | None = None

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: str = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    SMTP_EMAIL: str = "noreply@petworld.com"

    BREED_CACHE_TTL: int = 3600
    REDIS_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/0"

    MODE: str = "DEV"

    model_config = SettingsConfigDict(
        env_file=env_path,
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def db_url(self) -> str:
        return (
            self.DATABASE_URL
            or f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
               f"@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.POSTGRES_DB}"
        )

settings = Settings()