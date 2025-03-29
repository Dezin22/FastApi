# services/user.py
from dataclasses import dataclass
from fastapi import Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from core.db import get_db
from core.auth import create_token
from schemas.user import UserIn, TokenIn
from models.user import User


@dataclass
class UserService:
    db: Session = Depends(get_db)

    def create(self, user_in: UserIn) -> User:
        query = select(User).where(User.email == user_in.email)

        email_already_exists = (
            self.db.execute(query).scalars().first() is not None
        )

        if email_already_exists:
            raise HTTPException(
                detail='Já existe um usuário cadastrado com esse email.',
                status_code=status.HTTP_400_BAD_REQUEST
            )

        user = User(user_in.name, user_in.email, user_in.password)
        self.db.add(user)
        self.db.commit()

        return user
    
    def create_token(self, token_in: TokenIn) -> str:
        query = select(User).where(User.email == token_in.email)
        user = self.db.execute(query).scalars().first()
            
        if user is None or not user.verify_password(token_in.password):
            raise HTTPException(
                detail='Credênciais Inválidas.',
                status_code=status.HTTP_401_UNAUTHORIZED
            )
        
        return create_token(user.id)
    