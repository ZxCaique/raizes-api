from pydantic import BaseModel, EmailStr

from app.models.enums import PerfilUsuario


class UsuarioCreate(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    perfil: PerfilUsuario


class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    perfil: PerfilUsuario

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    email: EmailStr
    senha: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"