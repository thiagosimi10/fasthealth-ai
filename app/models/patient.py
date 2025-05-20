from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from core.database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    heart_rate = Column(Integer)
    blood_pressure = Column(Integer)
    glucose = Column(Float)
    symptoms = Column(String)

    predictions = relationship("RiskPrediction", back_populates="patient", cascade="all, delete")
