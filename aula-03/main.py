from fastapi import FastAPI, HTTPException, status
from schemas import UserOut,UserIn
from models import User
import db


users = []
app = FastAPI()

@app.get('/user')
def get_all_user() -> list[UserOut]:
    users = db.get_all_users()
    if len(users) == 0:
        raise HTTPException(status.HTTP_204_NO_CONTENT)
    return users

@app.get('/user/{id}')
def get_user_by_id(id: str) -> UserOut: # Definindo o Schema UserOut para esconder a senha.
		# Busca o usuário pelo ID
    user = db.get_by_id(id)

		# Se não encontrar, retorna o status code 404 (Not Found)
    if user is None:
        raise HTTPException(
            detail='Usuário não encontrado',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    # Se encontrar, retorna o usuário
    return user

@app.post('/user')
def create_new_user(user:UserIn):
    exist_user = db.get_by_email(user.email)
    
    if exist_user is not None:
        raise HTTPException(
            detail= 'Já existe um usuario com esse email',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    new_user = User(**user.model_dump())
    db.create_new_user(new_user)
    return { 'massage':'Usuário Cadastrado com Sucesso.'}

@app.put('/users/{id}')
def update_user(id: str, user: UserIn):
		# Busca o usuário pelo ID
    user_to_update = db.get_by_id(id)

		# Caso não encontrado, retorna 404 (Not Found)
    if user_to_update is None:
        raise HTTPException(
            detail='Usuário não encontrado',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    # Busca usuário pelo email
    exist_user = db.get_by_email(user.email)
    
    # Se ele existir, e for um usuário com o ID diferente do que nós estamos atualizando
    # Então retorna o status 400 (Bad Request)
    if exist_user is not None and exist_user.id != user_to_update.id:
        raise HTTPException(
            detail='Já existe um usuário cadastrado com esse email.',
            status_code=status.HTTP_400_BAD_REQUEST
        )
    
    # Atualiza o usuário com os dados enviados.
    user_to_update.email = user.email
    user_to_update.name = user.name
    user_to_update.password = user.password
    
    db.update_user(user_to_update)
    return {"message" : "Usuário atualizado com sucesso."}

@app.delete('/users/{id}')
def delete_by_id(id: str):
		# Busca o usuário pelo ID
    user = db.get_by_id(id)
		
		# Caso não encontrado, retorna 404 (Not Found)
    if user is None:
        raise HTTPException(
            detail='Usuário não encontrado',
            status_code=status.HTTP_404_NOT_FOUND
        )
    
    # Caso encontre, exclui o usuário.
    db.delete_user(id)
    return {"message" : "Usuário excluído com sucesso."}