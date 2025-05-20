from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.patient import PatientCreate, PatientOut
from repositories.patient_repository import PatientRepository
from services.patient_service import PatientService
from core.database import get_db

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.post("/", response_model=PatientOut)
async def create_patient_route(
    payload: PatientCreate,
    db: AsyncSession = Depends(get_db)
):
    service = PatientService(PatientRepository())
    result = await service.create_patient(payload, db)
    return result
