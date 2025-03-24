from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    imgsrc: str
products = []

@app.get("/")
async def root():
    return {"message": "App is running..."} # returns a JSON response

@app.get("/products/{product_id}")
async def get_product(product_id: int, response: Response):
    if 0 <= product_id < len(products):
        product = products[product_id]
        response.status_code = 200
        return {"status": "success", "data": product}
    else:
        response.status_code = 404
        return {"status": "failed"}

@app.get("/products/")
async def get_all_products():
    return {"status": "success", "data": products}

@app.post("/products/")
async def post_product(product: Product):
    products.append(product)
    return {"status": "success"}