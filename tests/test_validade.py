from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_validate_with_cpf():
    """Tests if a message containing a CPF is flagged as invalid (PII detected)."""
    # Test with formatted and unformatted CPF
    payloads = [
        {"message": "O solicitante do processo é o CPF 123.456.789-00."},
        {"message": "Dados do usuário: 98765432100"}
    ]
    for json_data in payloads:
        response = client.post("/validate", json=json_data)
        assert response.status_code == 200
        # Assuming your main.py returns 'inválido' when PII is found
        assert response.json() == {"status": "inválido"}

def test_validate_clean_text():
    """Tests if a message with no PII is flagged as valid."""
    response = client.post("/validate", json={"message": "Quais são os gastos com educação em 2025?"})
    assert response.status_code == 200
    assert response.json() == {"status": "válido"}