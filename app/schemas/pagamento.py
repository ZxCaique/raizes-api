from pydantic import BaseModel

from app.models.enums import StatusPagamento


class PagamentoCreate(BaseModel):
    pedido_id: int


class PagamentoResponse(BaseModel):
    id: int
    pedido_id: int
    gateway: str
    status: StatusPagamento
    valor: float
    codigo_transacao: str | None = None

    class Config:
        from_attributes = True