from pydantic import BaseModel
from typing import List, Optional

class PredictInput(BaseModel):
    age: int
    gender: str
    heart_rate: int
    blood_pressure: int
    glucose: Optional[float]
    symptoms: Optional[List[str]] = []

class PredictOutput(BaseModel):
    risk_level: str
    probability: float