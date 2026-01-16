# Acesso à Informação - Hackathon CGDF

Solução de **classificação automática de pedidos de acesso à informação (LAI)** para identificação de dados pessoais.
Projeto desenvolvido para o **1º Hackathon em Controle Social - Desafio Participa DF (Categoria 1)**.

---

## Como executar o projeto

### Requisitos

* **Python 3.11+**
* **Docker** e **Docker Compose**


### Executando localmente (modo desenvolvimento)

1. **Execute o comando docker no terminal:**

    ````bash
    docker compose -f docker-compose_dev.yml up --build
    ````
   
    ou 

> Simplesmente use os atalhos fornecidos no **Makefile**

2. **Acesse a aplicação:**

   * Documentação da API (Swagger UI): [http://localhost:55555/docs](http://localhost:55555/docs)
   * Rota raiz (health check): [http://localhost:55555/](http://localhost:55555/)

---

## Estrutura do Projeto

`````txt
.
├── app/                     # Código principal da aplicação FastAPI
│   └── main.py
├── tests/                   # Testes unitários (pytest)
├── infra                    # Dockerfiles de produção e desenvolvimento
├── docker-compose_dev.yml   # Configuração do ambiente de desenvolvimento
├── docker-compose_prod.yml  # Configuração do ambiente de produção
├── requirements.txt         # Dependências e ferramentas
├── pyproject.toml           # Configuração do Black e Ruff
└── .github/workflows/ci.yml # Pipeline de integração contínua
`````
---

## Política de Branches (Gitflow Simplificado)

| Branch      | Propósito                                | Deploy  |
| ----------- | ---------------------------------------- | ------- |
| `develop`   | Ambiente de desenvolvimento e integração | -       |
| `prod`      | Branch de produção — ativa o pipeline    | CI/CD |

* Commits enviados para a branch `prod` disparam automaticamente o pipeline de build, lint e testes no GitHub Actions.

---

## Formatação e Qualidade de Código

O projeto segue os padrões **PEP8** e utiliza ferramentas automáticas para manter a consistência do código:

| Ferramenta | Função                              | Comando              |
| ---------- | ----------------------------------- | -------------------- |
| Black      | Formata o código automaticamente    | `black .`            |
| Ruff       | Analisa e organiza imports (linter) | `ruff check . --fix` |
| Pytest     | Executa os testes unitários         | `pytest -v`          |

O arquivo `pyproject.toml` contém todas as configurações dessas ferramentas.

---

## Pipeline de Integração Contínua (GitHub Actions)

O pipeline é executado **somente na branch `prod`** e realiza as seguintes etapas:

| Etapa              | Descrição                                         |
| ------------------ | ------------------------------------------------- |
| Build              | Constrói a imagem Docker e inicia os containers   |
| Style (Black)      | Verifica se o código segue o padrão de formatação |
| Linter (Ruff)     | Executa a análise estática do código              |
| Unit Tests (Pytest) | Roda os testes automatizados                      |
| Shutdown         | Encerra os containers, mesmo em caso de falha     |

**Arquivo da pipeline:**
`.github/workflows/ci.yml`