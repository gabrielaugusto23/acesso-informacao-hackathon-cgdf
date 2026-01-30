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

## Swagger

![img.png](img.png)

> Para testar a API, acesse o Swagger e informe a mensagem no formato JSON.
Em seguida, clique em “Execute” para visualizar o resultado da validação.
>
> A API também pode ser consumida por outras ferramentas de sua preferência, como Postman ou Insomnia.

---

## Estrutura do Projeto

`````txt
.
├── .github/                       # Configurações de CI/CD
│   └── workflows/
│       └── ci.yml                 # Pipeline do GitHub Actions
│
├── app/                           # Código principal da aplicação
│   ├── main.py                    # Entry point da FastAPI
│   ├── validators/                # Validadores de dados pessoais
│   │   ├── IValidator.py          # Interface base (Chain of Responsibility)
│   │   ├── ValidationResult.py    # Estrutura de retorno dos validadores
│   │   ├── NameValidator.py       # Detecção de nomes (spaCy)
│   │   ├── CPFValidator.py        # Detecção de CPF
│   │   ├── RGValidator.py         # Detecção de RG
│   │   ├── PhoneValidator.py      # Detecção de telefone
│   │   └── EmailValidator.py      # Detecção de e-mail
│   └── DataValidationPipeline.py  # Pipeline encadeado de validação
│
├── tests/                         # Testes automatizados (pytest)
│   ├── test_CPFValidator.py
│   ├── test_RGValidator.py
│   ├── test_PhoneValidator.py
│   ├── test_EmailValidator.py
│   ├── test_NameValidator.py
│   └── test_validade.py           # Testes de textos válidos (sem dados pessoais)
│
├── .env                           # Variáveis de ambiente (não versionado)
├── .env.example                   # Exemplo de variáveis de ambiente
│
├── docker-compose_dev.yml         # Docker Compose (desenvolvimento)
├── docker-compose_prod.yml        # Docker Compose (produção)
│
├── Dockerfile_dev                 # Dockerfile para ambiente de desenvolvimento
├── Dockerfile_prod                # Dockerfile para ambiente de produção
│
├── Makefile                       # Atalhos para comandos comuns
├── requirements.txt               # Dependências do projeto
├── pyproject.toml                 # Configuração do Black, Ruff e Pytest
├── README.md                      # Documentação do projeto
└── .gitignore                     # Arquivos ignorados pelo Git
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