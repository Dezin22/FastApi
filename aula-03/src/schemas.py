from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class MessageOut(BaseModel):
    message : str


class UserIn(BaseModel):
    name : str
    email : EmailStr
    password : str

class UserOut(BaseModel):
    id : UUID
    name : str
    email : str
    fl_active : bool
    created_at : datetime
    
class ProductsIn(BaseModel):
    name: str
    description: str
    category: str
    amount: int

class ProductsOut(BaseModel):
    id: UUID
    name: str
    description: str
    category: str
    amount: int
    