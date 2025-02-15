from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime


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
    
class MessageOut(BaseModel):
    message : str