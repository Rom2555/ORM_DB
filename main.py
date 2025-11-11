import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Stock, Shop, Sale, Base


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


DSN = "postgresql://postgres:postgres@localhost:5432/orm_db"

engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)
session = Session()

# Загрузка тестовых данных
with open('test_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()


def get_shops_by_publisher():
    # Запрашиваем
    publisher_input = input("Введите имя или ID издателя: ").strip()

    # Определяем, что введено — имя или ID
    if publisher_input.isdigit():
        publisher_id = int(publisher_input)
        publisher = session.query(Publisher).filter(Publisher.id == publisher_id).first()
    else:
        publisher = session.query(Publisher).filter(Publisher.name == publisher_input).first()

    # Проверяем, найден ли издатель
    if not publisher:
        print("Издатель не найден.")
        return

    # Запрос
    query = (
        session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
        .join(Book.stocks)  # Book - Stock
        .join(Stock.sales)  # Stock - Sale
        .join(Stock.shop)  # Stock - Shop
        .filter(Book.publisher_id == publisher.id)
    )

    # Вывод результатов
    print(f"\nДанные о продажах книг издателя '{publisher.name}':\n")
    for title, shop_name, price, date_sale in query.all():
        print(f"{title} | {shop_name} | {price} | {date_sale}")


get_shops_by_publisher()

# Закрытие сессии
session.close()
