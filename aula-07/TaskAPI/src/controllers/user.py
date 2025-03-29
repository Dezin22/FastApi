# controllers/user.py
from fastapi import APIRouter, Depends
from core.auth import get_current_user
from schemas.message import MessageOut
from schemas.user import UserIn, UserOut, TokenIn, TokenOut
from models.user import User
from services.user import UserService


user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.get('/me')
def get_me_user(user: User = Depends(get_current_user)) -> UserOut:
    return user


@user_router.post('/')
def create_new_user(
    user_in: UserIn, 
    user_service: UserService = Depends(UserService)
) -> MessageOut:
    user_service.create(user_in)
    return MessageOut(message='Usuário cadastrado com sucesso.')


@user_router.post('/token')
def create_new_token(
    token_in: TokenIn,
    user_service: UserService = Depends(UserService)
) -> TokenOut:
    token = user_service.create_token(token_in)
    return TokenOut(access_token=token)
