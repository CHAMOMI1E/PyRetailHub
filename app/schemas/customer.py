from pydantic import BaseModel, EmailStr


class CustomerBase(BaseModel):
    class Config:
        extra = "allow"

    id: int
    firstName: str | None = None
    email: EmailStr | None = None
    createdAt: str | None = None