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


class shop(Base):
    __tablename__ = 'shop'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))


class sale(Base):
    __tablename__ = 'sale'
    id = sa.Column(sa.Integer, primary_key=True)
    price = sa.Column(sa.Float)
    date_sale = sa.Column(sa.Date)
    id_stock = sa.Column(sa.Integer, sa.ForeignKey('stock.id'))
    count = sa.Column(sa.Integer)


class stock(Base):
    id = sa.Column(sa.Integer, primary_key=True)
    id_book = sa.Column(sa.Integer, sa.ForeignKey('book.id'))
    id_shop = sa.Column(sa.Integer, sa.ForeignKey('shop.id'))
    count = sa.Column(sa.Integer)
