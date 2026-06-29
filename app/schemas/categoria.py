from pydantic import BaseModel


class CategoriaCreate(BaseModel):
    nome: str
    descricao: str | None = None


class CategoriaUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None = None


class CategoriaResponse(BaseModel):
    id: int
    nome: str
    descricao: str | None = None

    class Config:
        from_attributes = True