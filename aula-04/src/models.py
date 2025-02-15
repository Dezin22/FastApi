from pydantic import BaseModel, Field
from datetime import datetime, timezone
from enum import StrEnum


class Category(StrEnum):
    FOOD = 'ALIMENTO'
    CLEANING = 'LIMPEZA'
    HYGIENE = 'HIGIENE'
    ELETRONIC = 'ELETRONICOS'
    
class Products(BaseModel):
    id: int | None = None
    name: str
    description: str | None = None
    category: Category
    amount: int
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))