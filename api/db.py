from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from api.config import settings

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
