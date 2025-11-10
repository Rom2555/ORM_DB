import sqlalchemy as sa
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class publisher(Base):
    __tablename__ = 'publisher'
    id = sa.Column(sa.Integer, primary_key=True)


class book(Base):
    __tablename__ = 'book'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(255))
    id_publisher = sa.Column(sa.Integer, sa.ForeignKey('publisher.id'))


