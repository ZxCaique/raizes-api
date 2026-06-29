from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import usuario_logado
from app.models.cliente import Cliente
from app.schemas.cliente import (
    ClienteCreate,
    ClienteResponse,
    ClienteUpdate,
)

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)


@router.post("/", response_model=ClienteResponse)
def criar_cliente(
    dados: ClienteCreate,
    usuario=Depends(usuario_logado),
    db: Session = Depends(get_db)
):
    cliente = Cliente(**dados.model_dump())

    db.add(cliente)
    db.commit()
    db.refresh(cliente)

    return cliente


@router.get("/", response_model=list[ClienteResponse])
def listar_clientes(
    usuario=Depends(usuario_logado),
    db: Session = Depends(get_db)
):
    return db.query(Cliente).all()


@router.get("/{cliente_id}", response_model=ClienteResponse)
def buscar_cliente(
    cliente_id: int,
    usuario=Depends(usuario_logado),
    db: Session = Depends(get_db)
):
    cliente = db.query(Cliente).filter(
        Cliente.id == cliente_id
    ).first()

    if not cliente:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado."
        )

    return cliente


@router.put("/{cliente_id}", response_model=ClienteResponse)
def atualizar_cliente(
    cliente_id: int,
    dados: ClienteUpdate,
    usuario=Depends(usuario_logado),
    db: Session = Depends(get_db)
):
    cliente = db.query(Cliente).filter(
        Cliente.id == cliente_id
    ).first()

    if not cliente:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado."
        )

    atualizacoes = dados.model_dump(exclude_unset=True)

    for campo, valor in atualizacoes.items():
        setattr(cliente, campo, valor)

    db.commit()
    db.refresh(cliente)

    return cliente


@router.delete("/{cliente_id}")
def excluir_cliente(
    cliente_id: int,
    usuario=Depends(usuario_logado),
    db: Session = Depends(get_db)
):
    cliente = db.query(Cliente).filter(
        Cliente.id == cliente_id
    ).first()

    if not cliente:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado."
        )

    db.delete(cliente)
    db.commit()

    return {
        "mensagem": "Cliente removido com sucesso."
    }