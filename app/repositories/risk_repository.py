from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from models.risk_prediction import RiskPrediction

class IRiskRepository(ABC):
    @abstractmethod
    async def save(self, prediction: RiskPrediction, db: AsyncSession) -> RiskPrediction:
        pass

class RiskRepository(IRiskRepository):
    async def save(self, prediction: RiskPrediction, db: AsyncSession) -> RiskPrediction:
        db.add(prediction)
        await db.commit()
        await db.refresh(prediction)
        return prediction