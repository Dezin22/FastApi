from fastapi import FastAPI
from pydantic import BaseModel


class MenssageOut(BaseModel):
    message : str

app = FastAPI()

class UsuarioIn(BaseModel):
    name:str
    idade:int
    altura:float


usuarios = []



@app.get('/usuario')
def get_usuario():
    return usuarios
@app.post('/usuario')
def create_usuario(usuario:UsuarioIn)->MenssageOut:
    usuarios.append(usuario.model_dump)
    return{'menssage':'Usuario cadastrado com sucesso'}