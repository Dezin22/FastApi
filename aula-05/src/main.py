from fastapi import FastAPI
from models import Product
from schemas import ProductIn, ProductOut, MessageOut


products = []
app = FastAPI(title='Product API')


@app.get('/products')
def find_all_products() -> list[ProductOut]:
    return products

@app.post('/products')
def create_product(product_in: ProductIn) -> MessageOut:
    data = product_in.model_dump()
    product = Product(**data)
    
    # Mesma coisa que estamos fazendo acima
    # product = Product(
    #     name=product_in.name, 
    #     description=product_in.description,
    #     category=product_in.category,
    #     quantity=product_in.quantity
    # )
    
    products.append(product)
    return MessageOut(message='Produto cadastrado com sucesso.')