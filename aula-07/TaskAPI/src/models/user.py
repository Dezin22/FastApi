from core import security
from core.db import BaseModel, Long
from datetime import datetime, timezone
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.orm import Mapped


class User(BaseModel):
    __tablename__ = 'users'

    id: Mapped[int] = Column(Long, primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String(255), nullable=False)
    email: Mapped[str] = Column(String(255), nullable=False, unique=True)
    password: Mapped[str] = Column(String(255), nullable=False)
    fl_active: Mapped[bool] = Column(Boolean, nullable=False)
    created_at: Mapped[datetime] = Column(DateTime(timezone=True), nullable=False)

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = security.hash(password)
        self.fl_active = True
        self.created_at = datetime.now(timezone.utc)
    
    def verify_password(self, password: str) -> bool:
        return security.check_hash(password, self.password)

# class Task(BaseModel):
#     __tablename__ = 'tasks'