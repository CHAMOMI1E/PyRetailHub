from typing import List
from pydantic import BaseModel, ConfigDict, Field
from fastapi import Query

from app.schemas.customer import CustomerId


class OrderGet(BaseModel):
    customer_id: int = Query(..., description="ID клиента", example=1)
    page: int = Query(1, description="Номер страницы", example=1)
    limit: int = Query(20, description="Количество заказов", example=20)


class OrderItemOffer(BaseModel):
    name: str = Field(alias="displayName")


class OrderItem(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: int
    status: str
    offer: OrderItemOffer
    initialPrice: float
    quantity: int


class CreateOrderItem(BaseModel):
    productName: str
    quantity: int
    price: float


class Order(BaseModel):
    id: int
    status: str
    fromApi: bool
    totalSumm: float
    currency: str
    items: List[OrderItem]


class CreateOrder(BaseModel):
    customer: CustomerId
    number: str
    items: List[CreateOrderItem]


class CreateOrderResponse(BaseModel):
    success: bool
    id: int


class CreatePayment(BaseModel):
    orderId: int
    amount: float
    type: str = "create"
    status: str | None = "paid"
