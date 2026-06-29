from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import BaseModel

if TYPE_CHECKING:
    from app.models.produto import Produto
    from app.models.unidade import Unidade


class Estoque(BaseModel, Base):
    __tablename__ = "estoques"

    produto_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("produtos.id"),
        nullable=False
    )

    unidade_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("unidades.id"),
        nullable=False
    )

    quantidade: Mapped[int] = mapped_column(Integer, default=0)

    produto: Mapped[Produto] = relationship(back_populates="estoques")
    unidade: Mapped[Unidade] = relationship(back_populates="estoques")