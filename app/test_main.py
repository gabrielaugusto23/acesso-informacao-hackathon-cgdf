from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_redirect():
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "/docs"

def test_validate_message_valid():
    response = client.post("/validate", json={"message": "ok"})
    assert response.status_code == 200
    assert response.json() == {
        "status": "Válido",
        "validators_status": "None",
        "private_data": "None"
    }

def test_validate_message_case_insensitive():
    response = client.post("/validate", json={"message": "OK"})
    assert response.status_code == 200
    assert response.json() == {
        "status": "Válido",
        "validators_status": "None",
        "private_data": "None"
    }

def test_validate_message_invalid():
    response = client.post("/validate", json={"message": "anything else"})
    assert response.status_code == 200
    assert response.json() == {
        "status": "Válido",
        "validators_status": "None",
        "private_data": "None"
    }

def test_validate_with_cpf():
    response = client.post("/validate", json={"message": "Meu CPF é 123.456.789-00"})
    assert response.status_code == 200
    assert response.json() == {
        "status": "Inválido",
        "validators_status": "CPFValidator",
        "private_data": "VALOR CPF"
    }

def test_validate_clean_text():
    response = client.post("/validate", json={"message": "Gostaria de saber o orçamento da saúde."})
    assert response.status_code == 200
    assert response.json() == {
        "status": "Válido",
        "validators_status": "None",
        "private_data": "None"
    }