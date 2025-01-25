from fastapi import FastAPI
from pydantic import BaseModel


class MenssageOut(BaseModel):
    message : str



class AnimalIn(BaseModel):
    name:str
    type:str
    color:str

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
