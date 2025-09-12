from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_predict():
    response = client.post("/predict/", json={"features": [22.5, 60, 1012]})
    assert response.status_code == 200
    assert "prediction" in response.json()

def test_stations():
    response = client.get("/stations/")
    assert response.status_code == 200
    assert "stations" in response.json()

def test_reports():
    response = client.get("/reports?days=3")
    assert response.status_code == 200
    assert "reports" in response.json()
