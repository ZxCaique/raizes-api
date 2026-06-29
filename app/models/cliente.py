from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import BaseModel

if TYPE_CHECKING:
    from app.models.fidelidade import Fidelidade
    from app.models.pedido import Pedido


class Cliente(BaseModel, Base):
    __tablename__ = "clientes"

    nome: Mapped[str] = mapped_column(String(100), nullable=False)

    email: Mapped[str | None] = mapped_column(
        String(150),
        unique=True,
        nullable=True
    )

    telefone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    cpf: Mapped[str | None] = mapped_column(
        String(14),
        unique=True,
        nullable=True
    )

    aceitou_lgpd: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    pontos: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    pedidos: Mapped[list[Pedido]] = relationship(
        back_populates="cliente"
    )

    fidelidade: Mapped[Fidelidade | None] = relationship(
        back_populates="cliente",
        uselist=False
    )