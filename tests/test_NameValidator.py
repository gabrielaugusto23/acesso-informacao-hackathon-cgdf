from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_validate_with_person_name_simple():
    payloads = [
        {"message": "O solicitante João Silva realizou o pedido."},
        {"message": "Encaminhar resposta para Maria Santos."},
        {"message": "Carlos Eduardo Pereira assinou o documento."},
    ]

    for json_data in payloads:
        response = client.post("/validate", json=json_data)
        assert response.status_code == 200
        assert response.json()["status"] == "Inválido"
        assert response.json()["validators_status"] == "NameValidator"


def test_validate_with_person_name_with_prepositions():
    payloads = [
        {"message": "José da Silva solicitou acesso às informações."},
        {"message": "Maria dos Santos fez a requisição."},
        {"message": "Ana de Souza encaminhou o pedido."},
    ]

    for json_data in payloads:
        response = client.post("/validate", json=json_data)
        assert response.status_code == 200
        assert response.json()["status"] == "Inválido"
        assert response.json()["validators_status"] == "NameValidator"


def test_validate_with_person_name_in_middle_of_text():
    payloads = [
        {"message": "O pedido foi protocolado ontem por João Silva no sistema."},
        {"message": "Conforme informado por Maria Aparecida dos Santos, segue anexo."},
    ]

    for json_data in payloads:
        response = client.post("/validate", json=json_data)
        assert response.status_code == 200
        assert response.json()["status"] == "Inválido"
        assert response.json()["validators_status"] == "NameValidator"


def test_validate_with_uppercase_words_not_person():
    payloads = [
        {"message": "O PROJETO JOAO SILVA FOI APROVADO."},
        {"message": "UNIDADE MARIA SANTOS DE ATENDIMENTO"},
    ]

    for json_data in payloads:
        response = client.post("/validate", json=json_data)
        assert response.status_code == 200
        assert response.json()["status"] == "Válido"


def test_validate_with_system_or_object_names():
    payloads = [
        {"message": "Sistema Carlos foi atualizado ontem."},
        {"message": "Módulo Maria executou a tarefa corretamente."},
        {"message": "Servidor João respondeu com erro 500."},
    ]

    for json_data in payloads:
        response = client.post("/validate", json=json_data)
        assert response.status_code == 200
        assert response.json()["status"] == "Inválido"
