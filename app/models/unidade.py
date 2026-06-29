from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import BaseModel
from app.models.enums import TipoUnidade

if TYPE_CHECKING:
    from app.models.estoque import Estoque
    from app.models.pedido import Pedido


class Unidade(BaseModel, Base):
    __tablename__ = "unidades"

    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    cidade: Mapped[str] = mapped_column(String(100), nullable=False)
    estado: Mapped[str] = mapped_column(String(2), nullable=False)

    tipo: Mapped[TipoUnidade] = mapped_column(
        Enum(TipoUnidade),
        nullable=False
    )

    estoques: Mapped[list[Estoque]] = relationship(back_populates="unidade")
    pedidos: Mapped[list[Pedido]] = relationship(back_populates="unidade")