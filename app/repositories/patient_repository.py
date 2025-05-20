from abc import ABC, abstractmethod
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.patient import Patient

class IPatientRepository(ABC):
    @abstractmethod
    async def create(self, patient: Patient, db: AsyncSession) -> Patient:
        pass

class PatientRepository(IPatientRepository):
    async def create(self, patient: Patient, db: AsyncSession) -> Patient:
        db.add(patient)
        await db.commit()
        await db.refresh(patient)
        return patient