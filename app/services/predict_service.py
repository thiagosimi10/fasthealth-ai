from schemas.predict import PredictInput, PredictOutput
from models.risk_prediction import RiskPrediction
from repositories.risk_repository import RiskRepository

class RiskModel:
    def __init__(self):
        self.repo = RiskRepository()

    async def predict(self, data: PredictInput, db) -> PredictOutput:
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
        result = PredictOutput(risk_level=level, probability=prob)

        prediction = RiskPrediction(
            risk_level=result.risk_level,
            probability=result.probability
        )
        await self.repo.save(prediction, db)

        return result