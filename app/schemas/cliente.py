from pydantic import BaseModel, EmailStr


class ClienteCreate(BaseModel):
    nome: str
    email: EmailStr | None = None
    telefone: str | None = None
    cpf: str | None = None
    aceitou_lgpd: bool = False


class ClienteUpdate(BaseModel):
    nome: str | None = None
    email: EmailStr | None = None
    telefone: str | None = None
    cpf: str | None = None
    aceitou_lgpd: bool | None = None


class ClienteResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr | None = None
    telefone: str | None = None
    cpf: str | None = None
    aceitou_lgpd: bool
    pontos: int

    class Config:
        from_attributes = True