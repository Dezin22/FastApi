from fastapi import FastAPI
from pydantic import BaseModel


class MenssageOut(BaseModel):
    message : str



class AnimalIn(BaseModel):
    name:str
    type:str
    color:str

class Usuario(BaseModel):
    name:str
    idade:int
    altura:float

app = FastAPI()

animais = []
usuarios = []
@app.get('/animal')
def get_all_animais():
    return animais

@app.post('/animal')
def create_new_animal(animal:AnimalIn)->MenssageOut:
    animais.append(animal.model_dump())
    return{'menssage' : 'Animal cadastrado com sucesso'}
@app.get('/usuario')
def get_usuario():
    return usuarios
@app.post('/usuario')
def create_usuario(usuario:Usuario)->MenssageOut:
    usuarios.append(usuario.model_dump())
    return{'menssage':'Usuario cadastrado com sucesso'}