from sqlalchemy import Column
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

class User(BaseModel):
    """"定义数据模型"""
    table = 't_users'
    __tablename__= table
    id = Column(Integer, primary_key=True, comment='自增长id')
    phone = Column(VARCHAR(13), unique=True, nullable=False, comment='手机号码')
    nick_name = Column(VARCHAR(20), nullable=False, comment='昵称')

    def __init__(self, phone, nick_name = 'unknown'):
        self.phone = phone
        self.nick_name = nick_name

    def __repr__(self):
        return '<User %s, %s>' % (self.nick_name, self.phone)

# if __name__ == '__main__':
#     print(User('17606856771'))