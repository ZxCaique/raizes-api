from pydantic import BaseModel, ConfigDict, Field

from app.models.enums import CanalPedido, FormaPagamento, StatusPedido


class ItemPedidoCreate(BaseModel):
    produto_id: int = Field(alias="produtoId")
    quantidade: int

    model_config = ConfigDict(populate_by_name=True)


class PedidoCreate(BaseModel):
    cliente_id: int = Field(alias="clienteId")
    unidade_id: int = Field(alias="unidadeId")
    canal_pedido: CanalPedido = Field(alias="canalPedido")
    forma_pagamento: FormaPagamento = Field(alias="formaPagamento")
    itens: list[ItemPedidoCreate]

    model_config = ConfigDict(populate_by_name=True)


class ItemPedidoResponse(BaseModel):
    id: int
    produto_id: int = Field(alias="produtoId")
    quantidade: int
    preco_unitario: float = Field(alias="precoUnitario")
    subtotal: float

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class PedidoResponse(BaseModel):
    id: int
    cliente_id: int = Field(alias="clienteId")
    unidade_id: int = Field(alias="unidadeId")
    canal_pedido: CanalPedido = Field(alias="canalPedido")
    forma_pagamento: FormaPagamento = Field(alias="formaPagamento")
    status: StatusPedido
    valor_total: float = Field(alias="valorTotal")
    itens: list[ItemPedidoResponse] = []

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)


class AtualizarStatusPedido(BaseModel):
    status: StatusPedido