from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from core.database import Base

class RiskPrediction(Base):
    __tablename__ = "risk_predictions"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=True)
    risk_level = Column(String, nullable=False)
    probability = Column(Float, nullable=False)

    patient = relationship("Patient", back_populates="predictions")