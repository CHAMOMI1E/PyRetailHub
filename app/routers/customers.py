from typing import List
from fastapi import APIRouter

from app.schemas.customer import (
    CreateCustomerResponse,
    CustomerFilter,
    Customer,
    CustomerCreate,
)
from app.services.customers import get_customers_from_crm, create_customer_in_crm


router = APIRouter(prefix="/customers", tags=["Customers"])


@router.get("/", response_model=List[Customer])
async def get_customers(model: CustomerFilter = CustomerFilter.as_dependency()):
    return await get_customers_from_crm(model=model)


@router.post("/", response_model=CreateCustomerResponse)
async def create_customer(model: CustomerCreate):
    return await create_customer_in_crm(customer=model)
