from fastapi import FastAPI, Depends, HTTPException, status
from schemas import UserIn
from db import get_db
from models import User
from sqlalchemy import select
from sqlalchemy.orm import Session


app = FastAPI(title='Task API')


@app.post('/users')
def create_new_user(
    user_in: UserIn, 
    db: Session = Depends(get_db)
):
    query = select(User).where(User.email == user_in.email)

    email_already_exists = (
        db.execute(query).scalars().first() is not None
    )

    if email_already_exists:
        raise HTTPException(
            detail='Já existe um usuário cadastrado com esse email.',
            status_code=status.HTTP_400_BAD_REQUEST
        )

    user = User(user_in.name, user_in.email, user_in.password)
    db.add(user)
    db.commit()

    return { 'message': 'Usuário cadsatrado com sucesso.' }