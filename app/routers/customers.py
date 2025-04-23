from fastapi import APIRouter


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
async def get_customers():
    return {"message": "Hello World"}