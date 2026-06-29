from fastapi import FastAPI

from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Raízes do Nordeste API",
    version="1.0.0",
    description="Sistema de gerenciamento da Rede Raízes do Nordeste"
)


@app.get("/")
def home():

    return {
        "message": "API Raízes do Nordeste",
        "status": "Online"
    }