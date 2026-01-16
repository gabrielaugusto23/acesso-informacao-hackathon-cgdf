from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_validate_ok():
    response = client.post("/validate", json={"message": "ok"})
    assert response.status_code == 200
    assert response.json() == {"status": "válido"}


def test_validate_invalid():
    response = client.post("/validate", json={"message": "erro"})
    assert response.status_code == 200
    assert response.json() == {"status": "inválido"}
