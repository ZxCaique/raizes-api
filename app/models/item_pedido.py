from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import BaseModel

if TYPE_CHECKING:
    from app.models.pedido import Pedido
    from app.models.produto import Produto


class ItemPedido(BaseModel, Base):
    __tablename__ = "itens_pedido"

    pedido_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("pedidos.id"),
        nullable=False
    )

    produto_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("produtos.id"),
        nullable=False
    )

    quantidade: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    preco_unitario: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    subtotal: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    pedido: Mapped["Pedido"] = relationship(
        back_populates="itens"
    )

    produto: Mapped["Produto"] = relationship(
        back_populates="itens_pedido"
    )