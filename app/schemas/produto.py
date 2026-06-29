from pydantic import BaseModel


class ProdutoCreate(BaseModel):
    nome: str
    descricao: str | None = None
    preco: float
    categoria_id: int
    ativo: bool = True


class ProdutoUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None = None
    preco: float | None = None
    categoria_id: int | None = None
    ativo: bool | None = None


class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: str | None = None
    preco: float
    categoria_id: int
    ativo: bool

    class Config:
        from_attributes = True