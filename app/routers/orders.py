from fastapi import APIRouter, Depends

from app.schemas.orders import CreateOrder, CreateOrderResponse, OrderGet, Order, CreatePayment
from app.services.orders import (
    create_order_in_crm,
    create_payment_in_crm,
    get_orders_from_crm,
)


router = APIRouter(prefix="/oreders", tags=["Orders"])


@router.get("/", response_model=list[Order])
async def get_orders(model: OrderGet = Depends()):
    return await get_orders_from_crm(model=model)


@router.post("/", response_model=CreateOrderResponse)
async def create_order(model: CreateOrder):
    return await create_order_in_crm(model=model)


@router.post("/payments")
async def create_payment(model: CreatePayment) -> bool:
    return await create_payment_in_crm(model=model)
