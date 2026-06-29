from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.base import BaseModel

if TYPE_CHECKING:
    from app.models.categoria import Categoria
    from app.models.estoque import Estoque
    from app.models.item_pedido import ItemPedido


class Produto(BaseModel, Base):
    __tablename__ = "produtos"

    nome: Mapped[str] = mapped_column(String(100), nullable=False)
    descricao: Mapped[str | None] = mapped_column(String(255), nullable=True)
    preco: Mapped[float] = mapped_column(Float, nullable=False)
    ativo: Mapped[bool] = mapped_column(Boolean, default=True)

    categoria_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("categorias.id"),
        nullable=False
    )

    categoria: Mapped[Categoria] = relationship(back_populates="produtos")
    estoques: Mapped[list[Estoque]] = relationship(back_populates="produto")
    itens_pedido: Mapped[list[ItemPedido]] = relationship(back_populates="produto")