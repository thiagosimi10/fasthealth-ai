import pytest

@pytest.mark.asyncio
async def test_predict_low_risk(async_client):
    payload = {
        "heart_rate": 80,
        "blood_pressure": 120,
        "glucose": 95
    }

    response = await async_client.post("/predict/risk", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["risk_level"] == "low"
    assert 0 < data["probability"] <= 0.2
