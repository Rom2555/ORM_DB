import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = sa.Column(sa.Integer, primary_key=True)
    books = relationship('Book', back_populates='publisher')


class Book(Base):
    __tablename__ = 'book'
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(255))
    id_publisher = sa.Column(sa.Integer, sa.ForeignKey('publisher.id'))
    publisher = relationship('Publisher', back_populates='books')
    stocks = relationship('Stock', back_populates='book')  # ← один Book → много Stock


class Shop(Base):
    __tablename__ = 'shop'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(255))
    stocks = relationship('Stock', back_populates='shop')  # ← один Shop → много Stock


class Stock(Base):
    __tablename__ = 'stock'
    id = sa.Column(sa.Integer, primary_key=True)
    id_book = sa.Column(sa.Integer, sa.ForeignKey('book.id'))
    id_shop = sa.Column(sa.Integer, sa.ForeignKey('shop.id'))
    count = sa.Column(sa.Integer)
    book = relationship('Book', back_populates='stocks')  # ← один Book
    shop = relationship('Shop', back_populates='stocks')  # ← один Shop
    sales = relationship('Sale', back_populates='stock')  # ← один Stock → много Sale


class Sale(Base):
    __tablename__ = 'sale'
    id = sa.Column(sa.Integer, primary_key=True)
    price = sa.Column(sa.Float)
    date_sale = sa.Column(sa.Date)
    id_stock = sa.Column(sa.Integer, sa.ForeignKey('stock.id'))
    count = sa.Column(sa.Integer)
    stock = relationship('Stock', back_populates='sales')  # ← один Stock