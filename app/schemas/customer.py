from typing import List, Optional
from fastapi import Depends, Query
from datetime import date, timedelta, datetime
from pydantic import BaseModel, EmailStr, Field


class CustomerBase(BaseModel):
    firstName: str
    lastName: Optional[str] = None
    patronymic: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None


class Customer(CustomerBase):
    id: int
    createdAt: Optional[datetime]


class CustomerCreate(CustomerBase):
    pass


class CustomerFilter(BaseModel):
    ids: Optional[List[int]] = Field(
        None, title="Ids filter", description="Фильтр по id", example=[1, 2, 3]
    )

    name: Optional[str] = Field(
        None, title="Name filter", description="Фильтр по имени", example="John"
    )

    email: Optional[EmailStr] = Field(
        None,
        title="Email filter",
        description="Фильтр по email",
        example="user@example.com",
    )

    date_from: Optional[date] = Field(
        None, title="Date from", description="Начальная дата для фильтрации"
    )

    date_to: Optional[date] = Field(
        None, title="Date to", description="Конечная дата для фильтрации"
    )
    page: int = Field(..., ge=1)

    limit: int = Field(..., ge=1, le=100)

    @classmethod
    def as_dependency(cls):
        def factory(
            ids: Optional[List[int]] = Query(
                None, description="Фильтр по id", example=[1, 2, 3]
            ),
            name: Optional[str] = Query(
                None, example="Josh", description="Фильтр по имени"
            ),
            email: Optional[EmailStr] = Query(
                None, example="example@gmail.com", description="Фильтр по email"
            ),
            date_from: Optional[date] = Query(
                None, example=date.today(), description="Начальная дата для фильтрации"
            ),
            date_to: Optional[date] = Query(
                None,
                example=date.today() + timedelta(days=1),
                description="Конечная дата для фильтрации",
            ),
            page: int = Query(1, ge=1),
            limit: int = Query(20, ge=1, le=100),
        ):
            return cls(
                ids=ids,
                name=name,
                email=email,
                date_from=date_from,
                date_to=date_to,
                page=page,
                limit=limit,
            )

        return Depends(factory)


class CreateCustomerResponse(BaseModel):
    success: bool
    id: int
    errorMsg: str | None = None


class CustomerId(BaseModel):
    id: int = Field(..., ge=1)
