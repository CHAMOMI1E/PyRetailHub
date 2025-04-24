from fastapi import FastAPI
from app.routers import customers_router, orders_router


app = FastAPI(version="0.0.1b", title="PyRetailHub API", debug=True)
app.include_router(router=customers_router)
app.include_router(router=orders_router)


@app.get("/", tags=["Greeting"])
def root():
    return {"message": "PyRetailHub API"}
