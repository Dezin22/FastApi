from tinydb import TinyDB, Query
from models import User


# Criando Instância do TinyDB para manipular nosso banco de dados JSON
db = TinyDB('./database.json', indent=2)


# Função para buscar todos os usuários do nosso banco
def get_all_users() -> list[User]:
		# Do banco de dados, da tabela "users" busca todos os usuários
    users = db.table('users').all()
    
    # Com o list comprehenssion, para cada usuário (Documento) retornado, cria um objeto da nossa classe "User"
    return [User(**user) for user in users]
    
def create_new_user(user: User) -> None:
		# Cria o documento do usuário.
    user_document = user.model_dump()
    
    # Atualiza os valores para um tipo que ele pode salvar no JSON
    user_document.update({
        'id': str(user.id),
        'created_at': user.created_at.isoformat()
    })
    
    # Na tabela de usuários, insere o nosso documento.
    db.table('users').insert(user_document)
    
# Nova função para buscar usuário pelo email
def get_by_email(email: str) -> User | None:
    # Query Object do TinyDB para fazer pesquisa
    QUser = Query()
    # Pesquisando se existe algum usuário com o email informado, retorna uma lista
    result = db.table('users').search(QUser.email == email)
    
    # Se a lista estiver vazia, retorna None
    if len(result) == 0:
        return None
    
    # Se não, pega o primeiro valor (já que o email é para ser unico) e retorna um usuário.
    return User(**result[0])

def get_by_id(id: str) -> User | None:
		# Query Object do TinyDB para fazer pesquisa
    QUser = Query()
    
    # Busca na tabela de usuários, alguem que o campo ID seja igual
    result = db.table('users').search(QUser.id == id)
    
    # Se não houverem resultados, retorna None
    if len(result) == 0:
        return None
    
    # Se não, pega o primeiro valor e retorna um usuário.
    return User(**result[0])

def update_user(user: User) -> None:
		# Documento do usuário a atualizar
    user_document = user.model_dump()
    
    # Converte os campos para um formato que pode ser salvo.
    user_document.update({
        'id': str(user.id),
        'created_at': user.created_at.isoformat()
    })
	
		# Cria Query Object
    QUser = Query()
    
    # Atualiza o usuário com o documento onde o id é igual.
    db.table('users').update(user_document, QUser.id == user_document.get('id'))
    
def delete_user(id: str) -> None:
		# Cria Query Object do TinyDB para pesquisar
    QUser = Query()
    
    # Exclui usuário onde o ID for igual
    db.table('users').remove(QUser.id == id)