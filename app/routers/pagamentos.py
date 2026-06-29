import uuid

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import usuario_logado
from app.models.enums import StatusPagamento, StatusPedido
from app.models.pagamento import Pagamento
from app.models.pedido import Pedido
from app.schemas.pagamento import PagamentoCreate, PagamentoResponse

router = APIRouter(
    prefix="/pagamentos",
    tags=["Pagamentos"]
)


@router.post("/processar", response_model=PagamentoResponse)
def processar_pagamento(
    dados: PagamentoCreate,
    usuario=Depends(usuario_logado),
    db: Session = Depends(get_db)
):
    pedido = db.query(Pedido).filter(
        Pedido.id == dados.pedido_id
    ).first()

    if not pedido:
        raise HTTPException(
            status_code=404,
            detail="Pedido não encontrado."
        )

    pagamento_existente = db.query(Pagamento).filter(
        Pagamento.pedido_id == pedido.id
    ).first()

    if pagamento_existente:
        return pagamento_existente

    pagamento = Pagamento(
        pedido_id=pedido.id,
        valor=float(pedido.valor_total),
        status=StatusPagamento.APROVADO,
        codigo_transacao=str(uuid.uuid4())
    )

    pedido.status = StatusPedido.PAGO

    db.add(pagamento)
    db.commit()
    db.refresh(pagamento)

    return pagamento