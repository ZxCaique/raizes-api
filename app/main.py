from fastapi import FastAPI

from app.core.config import API_TITLE, API_VERSION
from app.core.database import Base, engine

from app.models import *  

app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
    description="API para gerenciamento da Rede Raízes do Nordeste."
)

Base.metadata.create_all(bind=engine)


@app.get("/", tags=["Sistema"])
def home():
    return {
        "mensagem": "Bem-vindo à API Raízes do Nordeste",
        "status": "online",
        "versao": API_VERSION
    }