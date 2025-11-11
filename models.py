from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Publisher(Base):
    __tablename__ = 'publisher'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    books = relationship('Book', back_populates='publisher')

    def __repr__(self):
        return f"<Publisher(id={self.id}, name='{self.name}')>"


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    publisher_id = Column(Integer, ForeignKey('publisher.id'), nullable=False)
    publisher = relationship('Publisher', back_populates='books')
    stocks = relationship('Stock', back_populates='book')

    def __repr__(self):
        return f"<Book(id={self.id}, title='{self.title}', publisher_id={self.publisher_id})>"


class Shop(Base):
    __tablename__ = 'shop'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    stocks = relationship('Stock', back_populates='shop')

    def __repr__(self):
        return f"<Shop(id={self.id}, name='{self.name}')>"


class Stock(Base):
    __tablename__ = 'stock'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('book.id'), nullable=False)
    shop_id = Column(Integer, ForeignKey('shop.id'), nullable=False)
    count = Column(Integer, nullable=False)
    book = relationship('Book', back_populates='stocks')
    shop = relationship('Shop', back_populates='stocks')
    sales = relationship('Sale', back_populates='stock')

    def __repr__(self):
        return f"<Stock(id={self.id}, book_id={self.book_id}, shop_id={self.shop_id}, count={self.count})>"


class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True)
    price = Column(Numeric(precision=10, scale=2), nullable=False)
    date_sale = Column(DateTime, nullable=False)
    count = Column(Integer, nullable=False)
    stock_id = Column(Integer, ForeignKey('stock.id'), nullable=False)
    stock = relationship('Stock', back_populates='sales')

    def __repr__(self):
        return f"<Sale(id={self.id}, price={self.price}, date_sale={self.date_sale}, count={self.count}, stock_id={self.stock_id})>"
