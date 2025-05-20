import pytest_asyncio
from fastapi import FastAPI
from httpx import AsyncClient
from main import app


@pytest_asyncio.fixture
async def async_client():
    async with AsyncClient(base_url="http://test", app=app) as client:
        yield client
