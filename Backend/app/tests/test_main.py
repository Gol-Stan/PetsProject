import sys
import pathlib

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR))

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from typing_extensions import override

from app.database import Base, get_db
from app.main import app
from app.config import settings

TEST_DATA_BASE = "sqlite+aiosqlite:///:memory:"
engine_test = create_async_engine(TEST_DATA_BASE, echo=True)
AsyncSessionTest = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)


async def override_get_db():
    async with AsyncSessionTest() as session:
        yield session


app.dependency_overrides[get_db()] = override_get_db

@pytest.fixture
async def client():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c

    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)