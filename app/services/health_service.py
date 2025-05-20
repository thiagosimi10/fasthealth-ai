import asyncpg
import aioredis
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import engine


class HealthService:
    def __init__(self, redis_url: str, pg_url: str):
        self.redis_url = redis_url
        self.pg_url = pg_url

    async def check_postgres(self) -> bool:
        try:
            async with engine.begin() as conn:
                await conn.execute("SELECT 1")
            return True
        except Exception:
            return False

    async def check_redis(self) -> bool:
        try:
            redis = await aioredis.from_url(self.redis_url)
            pong = await redis.ping()
            return pong is True
        except Exception:
            return False
