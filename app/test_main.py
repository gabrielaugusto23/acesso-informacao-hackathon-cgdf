from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_redirect():
    """Test that the root path redirects to documentation"""
    response = client.get("/", follow_redirects=False)
    # RedirectResponse usually returns a 307 Temporary Redirect
    assert response.status_code == 307
    assert response.headers["location"] == "/docs"


def test_validate_message_valid():
    """Test the 'ok' message which should return 'válido'"""
    response = client.post("/validate", json={"message": "ok"})
    assert response.status_code == 200
    assert response.json() == {"status": "válido"}


def test_validate_message_case_insensitive():
    """Test that 'OK' (uppercase) also works"""
    response = client.post("/validate", json={"message": "OK"})
    assert response.status_code == 200
    assert response.json() == {"status": "válido"}


def test_validate_message_invalid():
    """Test a wrong message which should return 'inválido'"""
    response = client.post("/validate", json={"message": "anything else"})
    assert response.status_code == 200
    assert response.json() == {"status": "inválido"}

def test_validate_with_cpf():
    # This should now return "inválido" because the CPFValidator will detect the PII
    response = client.post("/validate", json={"message": "Meu CPF é 123.456.789-00"})
    assert response.status_code == 200
    assert response.json() == {"status": "inválido"}

def test_validate_clean_text():
    # This remains "válido" as no PII is present
    response = client.post("/validate", json={"message": "Gostaria de saber o orçamento da saúde."})
    assert response.status_code == 200
    assert response.json() == {"status": "válido"}