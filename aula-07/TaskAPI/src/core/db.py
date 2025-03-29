# db.py
from config import settings
from sqlalchemy import create_engine, BigInteger, Integer
from sqlalchemy.orm import DeclarativeBase, sessionmaker


engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def get_db():
    session = SessionLocal()
    try:
        yield session
    except Exception as err:
        session.rollback()
        raise err
    finally:
        session.close()


class BaseModel(DeclarativeBase): 
    pass


Long = BigInteger().with_variant(Integer(), 'sqlite')
