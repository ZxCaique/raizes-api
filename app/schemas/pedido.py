from pydantic import BaseModel

from app.models.enums import StatusPedido


class ItemPedidoCreate(BaseModel):
    produto_id: int
    quantidade: int


class PedidoCreate(BaseModel):
    cliente_id: int
    unidade_id: int
    itens: list[ItemPedidoCreate]


class ItemPedidoResponse(BaseModel):
    id: int
    produto_id: int
    quantidade: int
    preco_unitario: float
    subtotal: float

    class Config:
        from_attributes = True


class PedidoResponse(BaseModel):
    id: int
    cliente_id: int
    unidade_id: int
    status: StatusPedido
    valor_total: float
    itens: list[ItemPedidoResponse] = []

    class Config:
        from_attributes = True


class AtualizarStatusPedido(BaseModel):
    status: StatusPedido