"""
test_api.py
-----------
Lightweight smoke tests for the FastAPI service using FastAPI's
TestClient (no running server required).

Run with:
    python test_api.py
"""

from fastapi.testclient import TestClient
from sklearn.datasets import load_breast_cancer

from main import app, N_FEATURES

client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"
    print("test_health passed")


def test_features():
    resp = client.get("/features")
    assert resp.status_code == 200
    assert resp.json()["n_features"] == N_FEATURES
    print("test_features passed")


def test_predict_valid():
    sample = load_breast_cancer().data[0].tolist()
    resp = client.post("/predict", json={"features": sample})
    assert resp.status_code == 200
    body = resp.json()
    assert body["predicted_class"] in ("malignant", "benign")
    assert 0.0 <= body["confidence"] <= 1.0
    print("test_predict_valid passed")


def test_predict_wrong_length():
    resp = client.post("/predict", json={"features": [1, 2, 3]})
    assert resp.status_code == 422
    print("test_predict_wrong_length passed")


def test_predict_missing_field():
    resp = client.post("/predict", json={})
    assert resp.status_code == 422
    print("test_predict_missing_field passed")


def test_predict_non_numeric():
    resp = client.post("/predict", json={"features": ["a"] * N_FEATURES})
    assert resp.status_code == 422
    print("test_predict_non_numeric passed")


if __name__ == "__main__":
    test_health()
    test_features()
    test_predict_valid()
    test_predict_wrong_length()
    test_predict_missing_field()
    test_predict_non_numeric()
    print("\nAll tests passed.")
