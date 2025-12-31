from fastapi import FastAPI
from .services.products import get_all_products

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "welcome"}

@app.get("/products")
def get_products():
    return get_all_products()

