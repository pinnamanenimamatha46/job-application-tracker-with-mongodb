from collections.abc import AsyncIterator

import pytest_asyncio
from httpx import ASGITransport, AsyncClient
from pymongo import AsyncMongoClient

from app.core.config import settings
from app.repositories.application_repository import (
    job_application_repository,
)
from main import app


TEST_DATABASE_NAME = "job_application_tracker_test"
TEST_COLLECTION_NAME = "job_applications"


@pytest_asyncio.fixture
async def test_database(
    monkeypatch,
) -> AsyncIterator[None]:
    """
    Connect the repository to a separate MongoDB test database.

    The real job_application_tracker database is never changed.
    """
    client = AsyncMongoClient(settings.mongodb_url)
    test_database = client[TEST_DATABASE_NAME]
    test_collection = test_database[TEST_COLLECTION_NAME]

    monkeypatch.setattr(
        job_application_repository,
        "collection",
        test_collection,
    )

    await test_database.drop_collection(TEST_COLLECTION_NAME)

    yield

    await test_database.drop_collection(TEST_COLLECTION_NAME)
    await client.close()


@pytest_asyncio.fixture
async def client(
    test_database,
) -> AsyncIterator[AsyncClient]:
    del test_database

    transport = ASGITransport(app=app)

    async with AsyncClient(
        transport=transport,
        base_url="http://test",
    ) as async_client:
        yield async_client