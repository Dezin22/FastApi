from fastapi import FastAPI, HTTPException, status
from schemas import MessageOut, ProductsIn, ProductsOut
from models import Products
import db

products = []
app = FastAPI()

@app.get('/products')
def get_all_products() -> list[ProductsOut]:
    users = db.get_all_products()
    if len(users) == 0:
        raise HTTPException(status.HTTP_204_NO_CONTENT)
    return users

@app.get('/products/{id}')
def get_products_by_id(id: str) -> ProductsOut: # Definindo o Schema UserOut para esconder a senha.
		# Busca o usuário pelo ID
    product = db.get_products_by_id(id)

		# Se não encontrar, retorna o status code 404 (Not Found)
    if product is None:
        raise HTTPException(
            detail='Produto não encontrado',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    # Se encontrar, retorna o usuário
    return product

@app.post('/products', status_code=status.HTTP_201_CREATED)
def create_new_product(product_in:ProductsIn):
    exist_product = db.get_by_name(product_in.name)
    
    if exist_product is not None:
        raise HTTPException(
            detail= 'Já existe um produto com esse nome',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    new_product = Products(**product_in.model_dump())
    db.create_new_product(new_product)
    return MessageOut(message='Produto cadastrado com sucesso.')