from fastapi import FastAPI, HTTPException, Query
from .services.products import get_all_products

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "welcome"}

@app.get("/products")
def list_product(name: str = Query(default=None, min_length=1, max_length=50, description="Search by product name")):
    products = get_all_products()
    if name :
        searched_query = name.strip().lower()
        products = [p for p in products if searched_query in p.get("name" , "").lower()]

    if not products:
        if name:
            raise HTTPException( status_code = 404 , detail=f"No product found matching name ={name}")
        
    total = len(products)

    return { "total" : total, "items" : products }
