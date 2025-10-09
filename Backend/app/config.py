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

    REDIS_URL: str = "redis://localhost:6379/0"
    SECRET_KEY: str = "dev_secret_key"

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