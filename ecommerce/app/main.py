from fastapi import FastAPI, HTTPException, Query, Path
from .services.products import get_all_products
from .schema.product import Product
app = FastAPI()

@app.get("/")
def root():
    return {"message" : "welcome"}

@app.get("/products")
def list_product(name: str = Query(default=None, min_length=1, max_length=50, description="Search by product name"),
sort_by_price : bool = Query(default=False, description="Sort products by price"),
order : str = Query(default="asc", description="Sort order when sort_by_price= true (asc, dec)" ),
limit : int = Query(default=10, ge=1, le=100, description="Number of items to return")
):
    products = get_all_products()
    if name :
        searched_query = name.strip().lower()
        products = [p for p in products if searched_query in p.get("name" , "").lower()]

    if not products:
        if name:
            raise HTTPException( status_code = 404 , detail=f"No product found matching name ={name}")
    if sort_by_price:
        reverse = (order == 'dec')
        products = sorted(products, key=lambda p: p.get("price", 0), reverse=reverse)
        
    total = len(products)
    products = products[0:limit]

    return { "total" : total, "items" : products, "limit" : limit }

@app.get("/products/{product_id}")
def get_product_by_id(product_id: str = Path( ..., min_length=36, max_length=36, description="UUID of Products", example="0005a4ea-ce3f-4dd7-bee0-f4bbb70fae6a" )):
    products = get_all_products()
    for product in products:
        if product["id"] == product_id:
            return product
    raise HTTPException(status_code=404 , detail="Product Not Found")

@app.post("/products" , status_code=201)
def create_products(product):
    return product
