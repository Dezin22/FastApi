from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from datetime import datetime, timezone


# Criando nossa clase que irá representar os usuários na nossa aplicação
class User(BaseModel):
    id: UUID = Field(default_factory=uuid4) # campo "id" do tipo UUID, valor padrão retorno da função "uuid4()"
    name: str # campo "name" do tipo string, obrigatório
    email: str # campo "email" do tipo string, obrigatório
    password: str # campo "password" do tipo string, obrigatório
    fl_active: bool = True # campo "fl_active" do tipo booleano, valor padrão "True"
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc)) # campo "created_at" do tipo data e hora, valor padrão o momento de criação do objeto

class Products(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: str
    category: str
    amount: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    