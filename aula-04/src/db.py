from tinydb import TinyDB, Query
from models import Products

db = TinyDB('./database.json', indent=2)

def get_all_products() -> list[Products]:
		# Do banco de dados, da tabela "users" busca todos os usuários
    products = db.table('products').all()
    
    # Com o list comprehenssion, para cada usuário (Documento) retornado, cria um objeto da nossa classe "User"
    return [Products(**product) for product in products]
    
def create_new_product(product:Products) -> None:
    product_document = product.model_dump()
    
    # Atualiza os valores para um tipo que ele pode salvar no JSON
    product_document.update({
        'id': str(product.id),
        'created_at': product.created_at.isoformat()
    })
    
    # Na tabela de usuários, insere o nosso documento.
    db.table('users').insert(product_document)

def get_products_by_id(id: str) -> Products | None:
    # Busca na tabela de usuários, alguem que o campo ID seja igual
    result = db.table('products').search(Query().id == id)
    
    # Se não houverem resultados, retorna None
    if len(result) == 0:
        return None
    
    # Se não, pega o primeiro valor e retorna um usuário.
    return Products(**result[0])

def update_products(product: Products) -> None:
		# Documento do usuário a atualizar
    product_document = product.model_dump()
    
    # Converte os campos para um formato que pode ser salvo.
    product_document.update({
        'id': str(product.id),
        'created_at': product.created_at.isoformat()
    })
    
    # Atualiza o usuário com o documento onde o id é igual.
    db.table('products').update(product_document, Query().id == product_document.get('id')) 

def get_by_name(name: str) -> Products | None:
    # Pesquisando se existe algum usuário com o email informado, retorna uma lista
    result = db.table('products').search(Query().name == name)
    
    # Se a lista estiver vazia, retorna None
    if len(result) == 0:
        return None
    
    # Se não, pega o primeiro valor (já que o email é para ser unico) e retorna um usuário.
    return Products(**result[0])