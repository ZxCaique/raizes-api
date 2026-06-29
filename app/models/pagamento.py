from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Enum, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import BaseModel
from app.models.enums import FormaPagamento, StatusPagamento

if TYPE_CHECKING:
    from app.models.pedido import Pedido


class Pagamento(BaseModel, Base):
    __tablename__ = "pagamentos"

    pedido_id: Mapped[int] = mapped_column(Integer, ForeignKey("pedidos.id"), nullable=False)

    forma_pagamento: Mapped[FormaPagamento] = mapped_column(
        Enum(FormaPagamento),
        nullable=False
    )

    gateway: Mapped[str] = mapped_column(String(100), default="Gateway Simulado")
    status: Mapped[StatusPagamento] = mapped_column(
        Enum(StatusPagamento),
        default=StatusPagamento.PENDENTE
    )

    valor: Mapped[float] = mapped_column(Float, nullable=False)
    codigo_transacao: Mapped[str | None] = mapped_column(String(120))

    pedido: Mapped["Pedido"] = relationship(back_populates="pagamento")