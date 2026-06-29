from pydantic import BaseModel, ConfigDict, Field

from app.models.enums import FormaPagamento, StatusPagamento


class PagamentoCreate(BaseModel):
    pedido_id: int = Field(alias="pedidoId")

    model_config = ConfigDict(populate_by_name=True)


class PagamentoResponse(BaseModel):
    id: int
    pedido_id: int = Field(alias="pedidoId")
    forma_pagamento: FormaPagamento = Field(alias="formaPagamento")
    gateway: str
    status: StatusPagamento
    valor: float
    codigo_transacao: str | None = Field(default=None, alias="codigoTransacao")

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)