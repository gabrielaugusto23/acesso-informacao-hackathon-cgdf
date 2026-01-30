from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_validate_with_email_valid_formats():
    payloads = [
        {"message": "Meu e-mail é joao.silva@email.com."},
        {"message": "Contato: maria_santos123@gmail.com"},
        {"message": "Encaminhar resposta para carlos@empresa.com.br"},
        {"message": "O solicitante informou o e-mail ana.pereira@outlook.com"},
    ]

    for json_data in payloads:
        response = client.post("/validate", json=json_data)
        assert response.status_code == 200
        assert response.json()["status"] == "Inválido"
        assert response.json()["validators_status"] == "EmailValidator"


def test_validate_with_email_uppercase_and_symbols():
    payloads = [
        {"message": "Email para contato: JOAO.SILVA@EMAIL.COM"},
        {"message": "Usuário: maria-dos.santos@gov.br"},
        {"message": "Resposta enviada para suporte_tecnico@empresa.org"},
    ]

    for json_data in payloads:
        response = client.post("/validate", json=json_data)
        assert response.status_code == 200
        assert response.json()["status"] == "Inválido"
        assert response.json()["validators_status"] == "EmailValidator"
