from fastapi import FastAPI

from app.core.config import API_TITLE, API_VERSION
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=API_TITLE,
    version=API_VERSION
)


@app.get("/", tags=["Sistema"])
def home():

    return {
        "mensagem": "Bem-vindo à API Raízes do Nordeste",
        "status": "online",
        "versao": API_VERSION
    }