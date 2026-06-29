from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import BaseModel

if TYPE_CHECKING:
    from app.models.cliente import Cliente


class Fidelidade(BaseModel, Base):
    __tablename__ = "fidelidades"

    cliente_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("clientes.id"),
        nullable=False
    )

    pontos_acumulados: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    nivel: Mapped[str] = mapped_column(
        String(50),
        default="Bronze"
    )

    cliente: Mapped["Cliente"] = relationship(
        back_populates="fidelidade"
    )