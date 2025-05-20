from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.predict import PredictInput, PredictOutput
from services.predict_service import RiskModel
from core.database import get_db

router = APIRouter(prefix="/predict", tags=["Prediction"])

@router.post("/risk", response_model=PredictOutput)
async def predict_risk(payload: PredictInput, db: AsyncSession = Depends(get_db)):
    model = RiskModel()
    return await model.predict(payload, db)