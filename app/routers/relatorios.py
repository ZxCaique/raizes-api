from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.cliente import Cliente
from app.models.estoque import Estoque
from app.models.pedido import Pedido
from app.models.produto import Produto
from app.models.unidade import Unidade

router = APIRouter(prefix="/relatorios", tags=["Relatórios"])


@router.get("/resumo")
def resumo_geral(db: Session = Depends(get_db)):
    return {
        "total_clientes": db.query(Cliente).count(),
        "total_produtos": db.query(Produto).count(),
        "total_unidades": db.query(Unidade).count(),
        "total_pedidos": db.query(Pedido).count(),
    }


@router.get("/vendas")
def relatorio_vendas(db: Session = Depends(get_db)):
    pedidos = db.query(Pedido).all()

    return {
        "quantidade_pedidos": len(pedidos),
        "valor_total_vendido": sum(p.valor_total for p in pedidos),
    }


@router.get("/estoque-baixo")
def relatorio_estoque_baixo(db: Session = Depends(get_db)):
    itens = db.query(Estoque).filter(Estoque.quantidade <= 5).all()

    return [
        {
            "estoque_id": item.id,
            "produto_id": item.produto_id,
            "unidade_id": item.unidade_id,
            "quantidade": item.quantidade,
        }
        for item in itens
    ]