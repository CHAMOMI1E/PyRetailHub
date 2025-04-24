import json
from typing import List
from app.schemas.customer import (
    CreateCustomerResponse,
    Customer,
    CustomerFilter,
    CustomerCreate,
)
from app.services.retail_crm import RetailCRM
from app.core.config import settings


async def get_customers_from_crm(model: CustomerFilter) -> List[Customer]:
    params = {"page": model.page, "limit": model.limit}
    if model.ids:
        params["filter[ids][]"] = model.ids
    if model.name:
        params["filter[name]"] = model.name
    if model.email:
        params["filter[email]"] = model.email
    if model.date_from:
        params["filter[dateFrom]"] = model.date_from.isoformat()
    if model.date_to:
        params["filter[dateTo]"] = model.date_to.isoformat()
    async with RetailCRM(
        subdomain=settings.SUBDOMAIN,
        api_key=settings.API_KEY,
    ) as client:
        data = await client.get("customers", params=params)
    return [Customer(**customer) for customer in data["customers"]]


async def create_customer_in_crm(customer: CustomerCreate) -> CreateCustomerResponse:
    customer_data = customer.model_dump()
    data = {"site": settings.SUBDOMAIN, "customer": json.dumps(customer_data)}
    async with RetailCRM(
        subdomain=settings.SUBDOMAIN,
        api_key=settings.API_KEY,
    ) as client:
        r = await client.post("customers/create", data=data)
    return CreateCustomerResponse(**r)
