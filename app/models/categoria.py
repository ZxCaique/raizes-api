from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import BaseModel

if TYPE_CHECKING:
    from app.models.produto import Produto


class Categoria(BaseModel, Base):
    __tablename__ = "categorias"

    nome: Mapped[str] = mapped_column(
        String(80),
        unique=True,
        nullable=False
    )

    descricao: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    produtos: Mapped[list[Produto]] = relationship(
        back_populates="categoria"
    )