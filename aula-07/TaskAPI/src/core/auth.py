# auth.py
import jwt
from config import settings
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy import select
from sqlalchemy.orm import Session
from db import get_db
from models.user import User


bearer_security = HTTPBearer()


def encode_token(payload: dict) -> str:
    return jwt.encode(payload, settings.TOKEN_SECRET, settings.ALGORITHM)


def decode_token(token: str):
    return jwt.decode(token, settings.TOKEN_SECRET, algorithms=[settings.ALGORITHM])


def create_token(user_id: int) -> str:
    initiated_at = datetime.now(timezone.utc)
    expires_on = initiated_at + timedelta(seconds=settings.EXPIRATION_SECONDS)
	
    token_payload = {
        'exp': expires_on, 
        'iat': initiated_at, 
        'sub': str(user_id)
    }
		
    access_token: str = encode_token(token_payload)
    return access_token


# Depêndencia para Exigir Autenticação
def get_current_user(
    db: Session = Depends(get_db), # Injeção de Depêndencias da sessão do banco de dados.
    auth: HTTPAuthorizationCredentials = Depends(bearer_security), # Injeção de Depêndencias da Segurança que Exige o Token via Bearer.
) -> User:
    # Decoficando o Token para obter o payload que foi criado na geração do Token
    try:
        payload: dict = decode_token(auth.credentials)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            detail='Token Expirado.', status_code=status.HTTP_401_UNAUTHORIZED
        )
    except jwt.PyJWTError:
        raise HTTPException(
            detail='Token inválido.', status_code=status.HTTP_401_UNAUTHORIZED
        )
		
    # Uma vez decodificado, pegamos o id do usuário
    user_id = int(payload.get('sub'))
    
    # Query para buscar o usuário pelo ID.
    query = select(User).where(User.id == user_id)
    
    # Buscando Usuário Pelo ID
    user = db.execute(query).scalars().first()

    if user is None:
        raise HTTPException(
            detail='Usuário não encontrado.',
            status_code=status.HTTP_401_UNAUTHORIZED,
        )

    # Retorna o Usuário Atual no Endpoint que Está Utilizando Autenticação
    return user