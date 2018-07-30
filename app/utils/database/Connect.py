from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.model.Stock import *
from app.model.User import *

engine = create_engine('postgresql+psycopg2://Dolphin:ex4bFH9bmMz@106.14.196.51:5432/Dolphin')
DBSession = sessionmaker(bind=engine)

def get_session():
    return DBSession()

def add_user(user):
    session = get_session()
    session.add(user)
    session.commit()

def query_user(phone):
    session = get_session()
    user = session.query(User).filter_by(phone=phone).first()
    print(user)
    return user

def add_stock_info(stock, session):
    session.add(stock)
    session.commit()

def query_stock_info(session):
    # for res in session.query(Stock).\
    #         filter(Stock.date == start):
    #     print(type(res))
    #     print(res)
    print(session.query(Stock).all())

# 执行创建表的语句
def create_tables(BaseModel):
    BaseModel.metadata.create_all(engine)

if __name__ == '__main__':
    # stock = Stock(code='002337')
    # query_stock_info('2018-07-03', '2018-07-05', get_session())
    # query_user(get_session())
    # user = User(phone='889988')
    # query_stock_info(session=get_session())
    user = query_user("17606856771")
    print(user != None)
    if(user != None):
        print(user != None)
    else:
        print("not found user...")