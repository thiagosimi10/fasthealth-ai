from schemas.patient import PatientCreate
from models.patient import Patient
from repositories.patient_repository import IPatientRepository

class PatientService:
    def __init__(self, repository: IPatientRepository):
        self.repository = repository

    async def create_patient(self, data: PatientCreate, db) -> Patient:
        patient = Patient(
            name=data.name,
            age=data.age,
            gender=data.gender,
            heart_rate=data.heart_rate,
            blood_pressure=data.blood_pressure,
            glucose=data.glucose,
            symptoms=",".join(data.symptoms or [])
        )
        return await self.repository.create(patient, db)