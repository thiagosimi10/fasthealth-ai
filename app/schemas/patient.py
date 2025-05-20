from pydantic import BaseModel
from typing import Optional, List

class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str
    heart_rate: int
    blood_pressure: int
    glucose: Optional[float]
    symptoms: Optional[List[str]]

class PatientOut(BaseModel):
    id: int
    name: str
    age: int
    gender: str

    class Config:
        orm_mode = True
