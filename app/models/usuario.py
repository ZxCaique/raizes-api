from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column

from app.core.database import Base
from app.models.base import BaseModel
from app.models.enums import PerfilUsuario


class Usuario(BaseModel, Base):
    __tablename__ = "usuarios"

    nome: Mapped[str] = mapped_column(String(100), nullable=False)

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False
    )

    senha: Mapped[str] = mapped_column(String(255), nullable=False)

    perfil: Mapped[PerfilUsuario] = mapped_column(
        Enum(PerfilUsuario),
        nullable=False
    )