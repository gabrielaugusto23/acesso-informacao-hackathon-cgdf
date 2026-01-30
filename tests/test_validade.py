from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_validate_with_cpf():
    payloads = [
        {"message": "O solicitante do processo é o CPF 123.456.789-00."},
        {"message": "Dados do usuário: 98765432100"},
    ]
    for json_data in payloads:
        response = client.post("/validate", json=json_data)
        assert response.status_code == 200
        assert response.json()["status"] == "Inválido"
        assert response.json()["validators_status"] == "CPFValidator"

def test_validate_clean_text():
    response = client.post("/validate", json={"message": "Quais são os gastos com educação?"})
    assert response.status_code == 200
    assert response.json()["status"] == "Válido"
