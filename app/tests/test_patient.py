import pytest

@pytest.mark.asyncio
async def test_create_patient(async_client):
    payload = {
        "name": "Maria",
        "age": 45,
        "gender": "female",
        "heart_rate": 85,
        "blood_pressure": 130,
        "glucose": 98,
        "symptoms": "fatigue"
    }

    response = await async_client.post("/patients/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Maria"
    assert data["age"] == 45
    assert "id" in data

@pytest.mark.asyncio
async def test_get_patient(async_client):
    response = await async_client.get("/patients/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Maria"
