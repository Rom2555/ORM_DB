import sqlalchemy as sa
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = sa.Column(sa.Integer, primary_key=True)
    books = sa.orm.relationship('Book', back_populates='publisher')

class Book(Base):
    __tablename__ = 'book'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(255))
    id_publisher = sa.Column(sa.Integer, sa.ForeignKey('publisher.id'))
    publisher = sa.orm.relationship('Publisher', back_populates='books')
    stocks = sa.orm.relationship('Stock', back_populates='books')

class Shop(Base):
    __tablename__ = 'shop'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))
    stocks = sa.orm.relationship('Stock', back_populates='shop')


class Sale(Base):
    __tablename__ = 'sale'
    id = sa.Column(sa.Integer, primary_key=True)
    price = sa.Column(sa.Float)
    date_sale = sa.Column(sa.Date)
    id_stock = sa.Column(sa.Integer, sa.ForeignKey('stock.id'))
    count = sa.Column(sa.Integer)
    stocks = sa.orm.relationship('Stock', back_populates='sales')


class Stock(Base):
    id = sa.Column(sa.Integer, primary_key=True)
    id_book = sa.Column(sa.Integer, sa.ForeignKey('book.id'))
    id_shop = sa.Column(sa.Integer, sa.ForeignKey('shop.id'))
    count = sa.Column(sa.Integer)
    shop = sa.orm.relationship('Shop', back_populates='stocks')
    sales = sa.orm.relationship('Sale', back_populates='stocks')
    books = sa.orm.relationship('Book', back_populates='stocks')