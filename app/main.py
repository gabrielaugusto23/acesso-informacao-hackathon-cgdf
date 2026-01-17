from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from app.chain.ChainOfResponsibility import PersonalDataChain

app = FastAPI(
    title="Acesso à Informação - CGDF",
    description=(
        "API desenvolvida para o Hackathon da CGDF.\n\n"
        "**Equipe:** João Antonio Ginuino Carvalho, João Igor e Gabriel Augusto.\n\n"
        "### Descrição da rota `/validate`:\n"
        "- **status = 'válido'** → significa que a mensagem está correta, sem problemas.\n"
        "- **status = 'inválido'** → significa que a mensagem contém erro ou formato incorreto."
    ),
    version="1.0.0",
)


class Message(BaseModel):
    message: str


class Status(BaseModel):
    status: str


@app.post(
    "/validate", response_model=Status, summary="Valida uma mensagem enviada pelo usuário"
)
def validate_message(data: Message):
    """
    Recebe uma mensagem e retorna um status:
    - **válido:** quando a mensagem está correta.
    - **inválido:** quando a mensagem apresenta algum problema.
    """

    # if data.message.lower() == "ok":
    #     return Status(status="válido")
    # return Status(status="inválido")

    chain = PersonalDataChain.build()

    if chain.handle(data.message.lower()):
        return Status(status="válido")
    else:
        Status(status="inválido")
        return None


@app.get("/", include_in_schema=False)
def root():
    """Redireciona para a documentação Swagger."""
    return RedirectResponse(url="/docs")


@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    """Redireciona rotas inexistentes para a documentação."""
    return RedirectResponse(url="/docs")
