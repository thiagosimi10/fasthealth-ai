from abc import ABC, abstractmethod
from app.schemas.predict import PredictInput, PredictOutput

class PredictionStrategy(ABC):
    @abstractmethod
    def predict(self, data: PredictInput) -> PredictOutput:
        pass