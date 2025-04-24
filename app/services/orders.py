import json
from typing import List
from app.schemas.orders import (
    CreateOrder,
    CreateOrderResponse,
    CreatePayment,
    OrderGet,
    Order,
)
from app.services.retail_crm import RetailCRM
from app.core.config import settings


async def get_orders_from_crm(model: OrderGet) -> List[Order]:
    data = {
        "filter[customerId]": model.customer_id,
        "page": model.page,
        "limit": model.limit,
    }
    async with RetailCRM(
        subdomain=settings.SUBDOMAIN,
        api_key=settings.API_KEY,
    ) as client:
        data = await client.get("orders", params=data)
    return [Order(**item) for item in data["orders"]]


async def create_order_in_crm(model: CreateOrder) -> CreateOrderResponse:
    data = {"site": settings.SUBDOMAIN, "order": json.dumps(model.model_dump())}
    async with RetailCRM(
        subdomain=settings.SUBDOMAIN,
        api_key=settings.API_KEY,
    ) as client:
        data = await client.post("orders/create", data=data)
    return CreateOrderResponse(**data)


async def create_payment_in_crm(model: CreatePayment):
    data = {
        "site": settings.SUBDOMAIN,
        "payment": json.dumps(
            {
                "amount": model.amount,
                "order": {"id": model.orderId},
                "status": model.status,
                "type": model.type,
            }
        ),
    }
    async with RetailCRM(
        subdomain=settings.SUBDOMAIN,
        api_key=settings.API_KEY,
    ) as client:
        data = await client.post("orders/payments/create", data=data)
    return True if data.get("success") else False
