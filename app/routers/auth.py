from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import (
    criar_token_acesso,
    gerar_hash_senha,
    verificar_senha,
)
from app.models.usuario import Usuario
from app.schemas.usuario import (
    LoginRequest,
    TokenResponse,
    UsuarioCreate,
    UsuarioResponse,
)

router = APIRouter(
    prefix="/auth",
    tags=["Autenticação"]
)


@router.post("/registrar", response_model=UsuarioResponse)
def registrar_usuario(
    dados: UsuarioCreate,
    db: Session = Depends(get_db)
):
    usuario_existente = db.query(Usuario).filter(
        Usuario.email == dados.email
    ).first()

    if usuario_existente:
        raise HTTPException(
            status_code=400,
            detail="E-mail já cadastrado."
        )

    usuario = Usuario(
        nome=dados.nome,
        email=dados.email,
        senha=gerar_hash_senha(dados.senha),
        perfil=dados.perfil
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario


@router.post("/login", response_model=TokenResponse)
def login(
    dados: LoginRequest,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.email == dados.email
    ).first()

    if not usuario:
        raise HTTPException(
            status_code=401,
            detail="Credenciais inválidas."
        )

    senha_valida = verificar_senha(
        dados.senha,
        usuario.senha
    )

    if not senha_valida:
        raise HTTPException(
            status_code=401,
            detail="Credenciais inválidas."
        )

    token = criar_token_acesso({
        "sub": usuario.email,
        "perfil": usuario.perfil.value
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }