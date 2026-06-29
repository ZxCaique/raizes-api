from pydantic import BaseModel


class FidelidadeResponse(BaseModel):
    id: int
    cliente_id: int
    pontos_acumulados: int
    nivel: str

    class Config:
        from_attributes = True