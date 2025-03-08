# db.py
from config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine(settings.DATABASE_URL)

# Criando a classe "SessionLocal" vinculada a engine 
# para abrir a sessão no banco que a engine está conectada
SessionLocal = sessionmaker(bind=engine) 


# Criando função "get_db" para que a gente possa abrir
# a sessão sempre que precisarmos
def get_db():
    session = SessionLocal()
    try:
		    # O "yield" retorna a sessão para onde utilizaremos
		    # e depois que a função que abrimos terminar ele volta para essa função
        yield session 
    except:
		    # Caso haja qualquer error, ele vai dar rollback na transação
        session.rollback()
    finally:
		    # Independente do resultado, ele sempre encerra a sessão
        session.close()
