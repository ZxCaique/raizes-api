from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Enum, Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import BaseModel
from app.models.enums import StatusPedido

if TYPE_CHECKING:
    from app.models.cliente import Cliente
    from app.models.item_pedido import ItemPedido
    from app.models.pagamento import Pagamento
    from app.models.unidade import Unidade


class Pedido(BaseModel, Base):
    __tablename__ = "pedidos"

    cliente_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("clientes.id"),
        nullable=False
    )

    unidade_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("unidades.id"),
        nullable=False
    )

    status: Mapped[StatusPedido] = mapped_column(
        Enum(StatusPedido),
        default=StatusPedido.CRIADO
    )

    valor_total: Mapped[float] = mapped_column(
        Float,
        default=0.0
    )

    cliente: Mapped["Cliente"] = relationship(
        back_populates="pedidos"
    )

    unidade: Mapped["Unidade"] = relationship(
        back_populates="pedidos"
    )

    itens: Mapped[list["ItemPedido"]] = relationship(
        back_populates="pedido",
        cascade="all, delete-orphan"
    )

    pagamento: Mapped["Pagamento | None"] = relationship(
        back_populates="pedido",
        uselist=False
    )