from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_validate_with_rg_valid_formats():
    payloads = [
        {"message": "Meu RG é 12.345.678-9."},
        {"message": "Identidade RJ-12.345.678-9 apresentada."},
        {"message": "Portador do RG SP12345678."},
    ]

    for json_data in payloads:
        response = client.post("/validate", json=json_data)
        assert response.status_code == 200
        assert response.json()["status"] == "Inválido"


def test_validate_with_rg_invalid_formats():
    payloads = [
        {"message": "Número do processo: 6.589.622"},
        {"message": "Valor total: 12.345.678"},
        {"message": "RG 1234567"},
        {"message": "Documento 12.345.678"},
    ]

    for json_data in payloads:
        response = client.post("/validate", json=json_data)
        assert response.status_code == 200
        assert response.json()["status"] == "Válido"


def test_validate_with_text_without_rg():
    response = client.post(
        "/validate",
        json={"message": "Quais são os gastos com saúde pública em 2023?"},
    )

    assert response.status_code == 200
    assert response.json()["status"] == "Válido"
