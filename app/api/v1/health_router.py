from fastapi import APIRouter
from app.services.health_service import HealthService
import os

router = APIRouter(prefix="/health", tags=["Health"])

@router.get("/status")
async def health_check():
    health = HealthService(
        redis_url=os.getenv("REDIS_URL", "redis://redis:6379"),
        pg_url=os.getenv("DATABASE_URL")
    )

    postgres_ok = await health.check_postgres()
    redis_ok = await health.check_redis()

    return {
        "postgres": postgres_ok,
        "redis": redis_ok,
        "status": postgres_ok and redis_ok
    }
