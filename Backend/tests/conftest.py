import asyncio
import os
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from dotenv import load_dotenv

load_dotenv('./')

from app.main import app
from app.database import Base, get_db
from app.config import settings

if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

TEST_DATABASE_URl = (
    f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
    f"@[{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.POSTGRES_DB}_test"
)


engine_test = create_async_engine(TEST_DATABASE_URl, echo=True, future=True)
TestingSessionLocal = async_sessionmaker(engine_test, expire_on_commit=False, class_=AsyncSession)


@pytest.fixture(scope="function")
async def async_session():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with TestingSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


@pytest.fixture(scope="function")
async def client(async_session: AsyncSession):
    async def override_get_db():
        try:
            yield async_session
        finally:
            await async_session.close()

        app.dependency_overrides[get_db] = override_get_db

        async  with AsyncClient(app=app, base_url="http://test") as ac:
            yield ac

        app.dependency_overrides.clear()