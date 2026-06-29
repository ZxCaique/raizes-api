from pydantic import BaseModel


class EstoqueCreate(BaseModel):
    produto_id: int
    unidade_id: int
    quantidade: int = 0


class EstoqueUpdate(BaseModel):
    quantidade: int


class EstoqueResponse(BaseModel):
    id: int
    produto_id: int
    unidade_id: int
    quantidade: int

    class Config:
        from_attributes = True