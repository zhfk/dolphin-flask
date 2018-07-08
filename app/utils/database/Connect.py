from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import app.model.Stock as Stock

engine = create_engine('postgresql+psycopg2://Dolphin:ex4bFH9bmMz@106.14.196.51:5432/Dolphin')
DBSession = sessionmaker(bind=engine)

def get_session():
    return DBSession()

def add_user(user, session):
    session.add(user)
    session.commit()

def add_stock_info(stock, session):
    session.add(stock)
    session.commit()

def query_stock_info(start, end, session):
    for res in session.query(Stock).\
            filter(Stock.date == start):
        print(type(res))
        print(res)

if __name__ == '__main__':
    # stock = Stock(code='002337')
    query_stock_info('2018-07-03', '2018-07-05', get_session())