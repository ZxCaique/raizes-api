from fastapi import FastAPI

from app.core.config import API_TITLE, API_VERSION
from app.core.database import Base, engine

from app.models import (
    Usuario,
    Cliente,
    Categoria,
    Produto,
    Unidade,
    Estoque,
    Pedido,
    ItemPedido,
    Pagamento,
    Fidelidade,
)

from app.routers import (
    auth,
    clientes,
    categorias,
    produtos,
    unidades,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
    description="API para gerenciamento da Rede Raízes do Nordeste."
)


@app.get("/", tags=["Sistema"])
def home():
    return {
        "mensagem": "Bem-vindo à API Raízes do Nordeste",
        "status": "online",
        "versao": API_VERSION
    }


app.include_router(auth.router)
app.include_router(clientes.router)
app.include_router(categorias.router)
app.include_router(produtos.router)
app.include_router(unidades.router)