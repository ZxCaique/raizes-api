from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import usuario_logado
from app.models.categoria import Categoria
from app.schemas.categoria import (
    CategoriaCreate,
    CategoriaResponse,
    CategoriaUpdate,
)

router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)


@router.post("/", response_model=CategoriaResponse)
def criar_categoria(
    dados: CategoriaCreate,
    usuario=Depends(usuario_logado),
    db: Session = Depends(get_db)
):
    categoria = Categoria(**dados.model_dump())

    db.add(categoria)
    db.commit()
    db.refresh(categoria)

    return categoria


@router.get("/", response_model=list[CategoriaResponse])
def listar_categorias(
    usuario=Depends(usuario_logado),
    db: Session = Depends(get_db)
):
    return db.query(Categoria).all()


@router.get("/{categoria_id}", response_model=CategoriaResponse)
def buscar_categoria(
    categoria_id: int,
    usuario=Depends(usuario_logado),
    db: Session = Depends(get_db)
):
    categoria = db.query(Categoria).filter(
        Categoria.id == categoria_id
    ).first()

    if not categoria:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada."
        )

    return categoria


@router.put("/{categoria_id}", response_model=CategoriaResponse)
def atualizar_categoria(
    categoria_id: int,
    dados: CategoriaUpdate,
    usuario=Depends(usuario_logado),
    db: Session = Depends(get_db)
):
    categoria = db.query(Categoria).filter(
        Categoria.id == categoria_id
    ).first()

    if not categoria:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada."
        )

    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(categoria, campo, valor)

    db.commit()
    db.refresh(categoria)

    return categoria


@router.delete("/{categoria_id}")
def excluir_categoria(
    categoria_id: int,
    usuario=Depends(usuario_logado),
    db: Session = Depends(get_db)
):
    categoria = db.query(Categoria).filter(
        Categoria.id == categoria_id
    ).first()

    if not categoria:
        raise HTTPException(
            status_code=404,
            detail="Categoria não encontrada."
        )

    db.delete(categoria)
    db.commit()

    return {
        "mensagem": "Categoria removida com sucesso."
    }