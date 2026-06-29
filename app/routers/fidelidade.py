from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.cliente import Cliente
from app.models.fidelidade import Fidelidade
from app.schemas.fidelidade import FidelidadeResponse

router = APIRouter(prefix="/fidelidade", tags=["Fidelidade"])


@router.post("/{cliente_id}/criar", response_model=FidelidadeResponse)
def criar_fidelidade(cliente_id: int, db: Session = Depends(get_db)):
    cliente = db.query(Cliente).filter(Cliente.id == cliente_id).first()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")

    fidelidade = db.query(Fidelidade).filter(
        Fidelidade.cliente_id == cliente_id
    ).first()

    if fidelidade:
        return fidelidade

    fidelidade = Fidelidade(
        cliente_id=cliente_id,
        pontos_acumulados=cliente.pontos,
        nivel="Bronze"
    )

    db.add(fidelidade)
    db.commit()
    db.refresh(fidelidade)

    return fidelidade


@router.get("/{cliente_id}", response_model=FidelidadeResponse)
def buscar_fidelidade(cliente_id: int, db: Session = Depends(get_db)):
    fidelidade = db.query(Fidelidade).filter(
        Fidelidade.cliente_id == cliente_id
    ).first()

    if not fidelidade:
        raise HTTPException(status_code=404, detail="Fidelidade não encontrada.")

    return fidelidade


@router.post("/{cliente_id}/adicionar-pontos", response_model=FidelidadeResponse)
def adicionar_pontos(
    cliente_id: int,
    pontos: int,
    db: Session = Depends(get_db)
):
    fidelidade = db.query(Fidelidade).filter(
        Fidelidade.cliente_id == cliente_id
    ).first()

    if not fidelidade:
        raise HTTPException(status_code=404, detail="Fidelidade não encontrada.")

    fidelidade.pontos_acumulados += pontos

    if fidelidade.pontos_acumulados >= 1000:
        fidelidade.nivel = "Ouro"
    elif fidelidade.pontos_acumulados >= 500:
        fidelidade.nivel = "Prata"
    else:
        fidelidade.nivel = "Bronze"

    db.commit()
    db.refresh(fidelidade)

    return fidelidade