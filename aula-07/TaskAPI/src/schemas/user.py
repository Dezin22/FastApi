from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: str
    fl_active: bool
    created_at: datetime


class TokenIn(BaseModel):
    email: str
    password: str


class TokenOut(BaseModel):
    access_token: str
    type: str = 'bearer'