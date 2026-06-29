from pydantic import BaseModel

from app.models.enums import TipoUnidade


class UnidadeCreate(BaseModel):
    nome: str
    cidade: str
    estado: str
    tipo: TipoUnidade


class UnidadeUpdate(BaseModel):
    nome: str | None = None
    cidade: str | None = None
    estado: str | None = None
    tipo: TipoUnidade | None = None


class UnidadeResponse(BaseModel):
    id: int
    nome: str
    cidade: str
    estado: str
    tipo: TipoUnidade

    class Config:
        from_attributes = True