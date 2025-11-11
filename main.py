import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Publisher, Book, Stock, Shop, Sale, Base




def create_tables(engine):
    Base.metadata.create_all(engine)


DSN = "postgresql://postgres:postgres@localhost:5432/orm_db"

engine = sqlalchemy.create_engine(DSN)


create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)
session = Session()