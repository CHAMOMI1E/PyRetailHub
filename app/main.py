from fastapi import FastAPI


app = FastAPI(version="0.0.1b", title="PyRetailHub API", debug=True)





@app.get("/", tags=["Greeting"])
def root():
    return {"message": "PyRetailHub API"}