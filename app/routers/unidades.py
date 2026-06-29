from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.unidade import Unidade
from app.schemas.unidade import UnidadeCreate, UnidadeUpdate, UnidadeResponse

router = APIRouter(prefix="/unidades", tags=["Unidades"])


@router.post("/", response_model=UnidadeResponse)
def criar_unidade(dados: UnidadeCreate, db: Session = Depends(get_db)):
    unidade = Unidade(**dados.model_dump())
    db.add(unidade)
    db.commit()
    db.refresh(unidade)
    return unidade


@router.get("/", response_model=list[UnidadeResponse])
def listar_unidades(db: Session = Depends(get_db)):
    return db.query(Unidade).all()


@router.get("/{unidade_id}", response_model=UnidadeResponse)
def buscar_unidade(unidade_id: int, db: Session = Depends(get_db)):
    unidade = db.query(Unidade).filter(Unidade.id == unidade_id).first()

    if not unidade:
        raise HTTPException(status_code=404, detail="Unidade não encontrada.")

    return unidade


@router.put("/{unidade_id}", response_model=UnidadeResponse)
def atualizar_unidade(
    unidade_id: int,
    dados: UnidadeUpdate,
    db: Session = Depends(get_db)
):
    unidade = db.query(Unidade).filter(Unidade.id == unidade_id).first()

    if not unidade:
        raise HTTPException(status_code=404, detail="Unidade não encontrada.")

    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(unidade, campo, valor)

    db.commit()
    db.refresh(unidade)

    return unidade


@router.delete("/{unidade_id}")
def excluir_unidade(unidade_id: int, db: Session = Depends(get_db)):
    unidade = db.query(Unidade).filter(Unidade.id == unidade_id).first()

    if not unidade:
        raise HTTPException(status_code=404, detail="Unidade não encontrada.")

    db.delete(unidade)
    db.commit()

    return {"mensagem": "Unidade removida com sucesso."}