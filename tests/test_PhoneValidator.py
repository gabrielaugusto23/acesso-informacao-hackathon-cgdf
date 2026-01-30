from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_validate_with_phone_valid_formats():
    payloads = [
        {"message": "Telefone para contato: (61) 91234-5678."},
        {"message": "Meu número é 61912345678."},
        {"message": "Ligar para (11) 3456-7890 amanhã."},
        {"message": "Contato: 21 99876-5432"},
    ]

    for json_data in payloads:
        response = client.post("/validate", json=json_data)
        assert response.status_code == 200
        assert response.json()["status"] == "Inválido"
        assert response.json()["validators_status"] == "PhoneValidator"


def test_validate_with_phone_invalid_formats():
    payloads = [
        {"message": "Número do processo: 123456789"},
        {"message": "Ano 20231234 foi registrado."},
        # {"message": "Código interno 619123"},
    ]

    for json_data in payloads:
        response = client.post("/validate", json=json_data)
        assert response.status_code == 200
        assert response.json()["status"] == "Inválido"


def test_validate_with_text_without_phone():
    response = client.post(
        "/validate",
        json={"message": "Solicito informações sobre contratos vigentes."},
    )

    assert response.status_code == 200
    assert response.json()["status"] == "Válido"
