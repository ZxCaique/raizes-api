from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload

from app.core.database import get_db
from app.models.estoque import Estoque
from app.models.item_pedido import ItemPedido
from app.models.pedido import Pedido
from app.models.produto import Produto
from app.schemas.pedido import AtualizarStatusPedido, PedidoCreate, PedidoResponse

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.post("/", response_model=PedidoResponse)
def criar_pedido(dados: PedidoCreate, db: Session = Depends(get_db)):
    if not dados.itens:
        raise HTTPException(
            status_code=400,
            detail="O pedido precisa ter pelo menos um item."
        )

    try:
        pedido = Pedido(
            cliente_id=dados.cliente_id,
            unidade_id=dados.unidade_id,
            valor_total=0.0
        )

        db.add(pedido)
        db.flush()

        valor_total = 0.0

        for item in dados.itens:
            produto = db.query(Produto).filter(
                Produto.id == item.produto_id
            ).first()

            if not produto:
                raise HTTPException(
                    status_code=404,
                    detail=f"Produto {item.produto_id} não encontrado."
                )

            estoque = db.query(Estoque).filter(
                Estoque.produto_id == item.produto_id,
                Estoque.unidade_id == dados.unidade_id
            ).first()

            if not estoque or estoque.quantidade < item.quantidade:
                raise HTTPException(
                    status_code=400,
                    detail=f"Estoque insuficiente para o produto {produto.nome}."
                )

            subtotal = float(produto.preco) * item.quantidade
            valor_total += subtotal
            estoque.quantidade -= item.quantidade

            item_pedido = ItemPedido(
                pedido_id=pedido.id,
                produto_id=produto.id,
                quantidade=item.quantidade,
                preco_unitario=float(produto.preco),
                subtotal=subtotal
            )

            db.add(item_pedido)

        pedido.valor_total = valor_total

        db.commit()

        pedido_salvo = db.query(Pedido).options(
            selectinload(Pedido.itens)
        ).filter(
            Pedido.id == pedido.id
        ).first()

        return pedido_salvo

    except HTTPException:
        db.rollback()
        raise

    except Exception as erro:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao criar pedido: {str(erro)}"
        )


@router.get("/", response_model=list[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    return db.query(Pedido).options(
        selectinload(Pedido.itens)
    ).all()


@router.get("/{pedido_id}", response_model=PedidoResponse)
def buscar_pedido(pedido_id: int, db: Session = Depends(get_db)):
    pedido = db.query(Pedido).options(
        selectinload(Pedido.itens)
    ).filter(
        Pedido.id == pedido_id
    ).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado.")

    return pedido


@router.patch("/{pedido_id}/status", response_model=PedidoResponse)
def atualizar_status(
    pedido_id: int,
    dados: AtualizarStatusPedido,
    db: Session = Depends(get_db)
):
    pedido = db.query(Pedido).filter(Pedido.id == pedido_id).first()

    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado.")

    pedido.status = dados.status

    db.commit()
    db.refresh(pedido)

    return pedido