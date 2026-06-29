from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import usuario_logado
from app.models.estoque import Estoque
from app.schemas.estoque import (
    EstoqueCreate,
    EstoqueResponse,
    EstoqueUpdate,
)

router = APIRouter(
    prefix="/estoque",
    tags=["Estoque"]
)


@router.post("/", response_model=EstoqueResponse)
def criar_estoque(
    dados: EstoqueCreate,
    usuario=Depends(usuario_logado),
    db: Session = Depends(get_db)
):
    estoque_existente = db.query(Estoque).filter(
        Estoque.produto_id == dados.produto_id,
        Estoque.unidade_id == dados.unidade_id
    ).first()

    if estoque_existente:
        raise HTTPException(
            status_code=400,
            detail="Estoque já cadastrado para este produto nesta unidade."
        )

    estoque = Estoque(**dados.model_dump())

    db.add(estoque)
    db.commit()
    db.refresh(estoque)

    return estoque


@router.get("/", response_model=list[EstoqueResponse])
def listar_estoque(
    usuario=Depends(usuario_logado),
    db: Session = Depends(get_db)
):
    return db.query(Estoque).all()


@router.put("/{estoque_id}", response_model=EstoqueResponse)
def atualizar_estoque(
    estoque_id: int,
    dados: EstoqueUpdate,
    usuario=Depends(usuario_logado),
    db: Session = Depends(get_db)
):
    estoque = db.query(Estoque).filter(
        Estoque.id == estoque_id
    ).first()

    if not estoque:
        raise HTTPException(
            status_code=404,
            detail="Estoque não encontrado."
        )

    estoque.quantidade = dados.quantidade

    db.commit()
    db.refresh(estoque)

    return estoque


@router.delete("/{estoque_id}")
def excluir_estoque(
    estoque_id: int,
    usuario=Depends(usuario_logado),
    db: Session = Depends(get_db)
):
    estoque = db.query(Estoque).filter(
        Estoque.id == estoque_id
    ).first()

    if not estoque:
        raise HTTPException(
            status_code=404,
            detail="Estoque não encontrado."
        )

    db.delete(estoque)
    db.commit()

    return {
        "mensagem": "Estoque removido com sucesso."
    }