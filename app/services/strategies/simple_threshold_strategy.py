from app.schemas.predict import PredictInput, PredictOutput
from .base_strategy import PredictionStrategy

class SimpleThresholdStrategy(PredictionStrategy):
    def predict(self, data: PredictInput) -> PredictOutput:
        score = sum([
            data.blood_pressure > 140,
            data.heart_rate > 100,
            data.glucose > 125
        ])
        levels = {
            0: ("low", 0.1),
            1: ("moderate", 0.6),
            2: ("high", 0.9),
            3: ("high", 0.9)
        }
        level, prob = levels.get(score, ("low", 0.1))
        return PredictOutput(risk_level=level, probability=prob)