import pytest
from app import app
import json

@pytest.fixture
def client():
    return app.test_client()

def test_ping(client):
    resp = client.get("/ping")
    assert resp.status_code == 200


def test_pred(client):
    test_data = {
        
        "company": "Maruti",
        "model_name": "Swift",
        "year": 2019,
        "kms_driven": 100,
        "fuel_type": "Petrol"
        
    }
    resp = client.post("/predict", json = test_data)
    print("hwwllll", resp.json)
    assert resp.status_code == 200
    assert resp.json == {"Predicted price of your car": 458894.10960853}



