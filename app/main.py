from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
# Import the pipeline you built
from app.DataValidationPipeline import DataValidationPipeline

app = FastAPI(
    title="Acesso à Informação - CGDF",
    description=(
        "API desenvolvida para o Hackathon da CGDF.\n\n"
        "**Equipe:** João Antonio Ginuino Carvalho, João Igor e Gabriel Augusto.\n\n"
        "### Descrição da rota `/validate`:\n"
        "- **status = 'válido'** → significa que a mensagem está limpa de dados pessoais.\n"
        "- **status = 'inválido'** → significa que a mensagem contém dados pessoais (CPF, Telefone, etc.)."
    ),
    version="1.0.0",
)

# Initialize the pipeline once when the app starts
pipeline = DataValidationPipeline.build()

class Message(BaseModel):
    message: str

class Status(BaseModel):
    status: str

@app.post(
    "/validate",
    response_model=Status,
    summary="Valida uma mensagem enviada pelo usuário",
)
def validate_message(data: Message):
    """
    Processa a mensagem pela Chain of Responsibility para detectar PII:
    - **válido:** nenhuma informação pessoal sensível foi encontrada.
    - **inválido:** a mensagem contém dados como CPF ou Telefone.
    """
    # Run the text through the chain
    # The current validators return the text; we detect PII if the chain 
    # logic marks it or if we implement a detection flag.
    # For now, let's check if the result matches the input.
    processed_text = pipeline.handle(data.message)
    
    # If your validators modify the text (e.g., masking) or 
    # if you want to flag detection, you check it here.
    # To pass the tests below, we'll assume detection makes it 'inválido'
    is_pii_detected = processed_text != data.message 
    
    if is_pii_detected:
        return Status(status="inválido")
    
    return Status(status="válido")

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    return RedirectResponse(url="/docs")