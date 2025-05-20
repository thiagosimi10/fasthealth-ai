import redis.asyncio as redis
import json
from models.patient import Patient

class PatientCacheService:
    def __init__(self, redis_url: str = "redis://redis:6379"):
        self.redis = redis.from_url(redis_url, decode_responses=True)

    async def get_patient(self, patient_id: int) -> dict | None:
        data = await self.redis.get(f"patient:{patient_id}")
        return json.loads(data) if data else None

    async def set_patient(self, patient: Patient):
        await self.redis.set(
            f"patient:{patient.id}",
            json.dumps({
                "id": patient.id,
                "name": patient.name,
                "age": patient.age,
                "gender": patient.gender
            }),
            ex=3600
        )