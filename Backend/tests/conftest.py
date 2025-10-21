# tests/conftest.py
import asyncio
import os
import pytest
import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.main import app
from app.database import Base, get_db

# ---- Для Windows + asyncpg ----
if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# ---- Настройки тестовой БД ----
TEST_DB_USER = os.getenv("DB_USER", "postgres")
TEST_DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
TEST_DB_HOST = os.getenv("DB_HOST", "localhost")  # контейнер Docker должен быть доступен
TEST_DB_PORT = os.getenv("DB_PORT", "5432")
TEST_DB_NAME = os.getenv("DB_NAME", "pets_test")

DATABASE_URL = f"postgresql+asyncpg://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{TEST_DB_HOST}:{TEST_DB_PORT}/{TEST_DB_NAME}"

# ---- Создаем async engine и сессию для тестов ----
engine_test = create_async_engine(DATABASE_URL, echo=False, future=True)
TestingSessionLocal = async_sessionmaker(engine_test, expire_on_commit=False)

# ---- Фикстура для переопределения сессии ----
@pytest_asyncio.fixture()
async def async_session():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    async with TestingSessionLocal() as session:
        yield session

# ---- Переопределяем зависимость FastAPI get_async_session ----
@pytest_asyncio.fixture()
async def client(async_session: AsyncSession):
    async def override_get_session():
        yield async_session

    app.dependency_overrides[get_db] = override_get_session

    async with AsyncClient(app=app, base_url="http://localhost:8000") as c:
        yield c

    app.dependency_overrides.clear()
