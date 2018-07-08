from sqlalchemy import Column
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()

"""
CREATE TABLE "public"."t_stock" (
	"id" SERIAL primary key,
	"code" varchar(8) NOT NULL,
	"autype" varchar(8) NOT NULL,
	"index" bool NOT NULL,
	"date" date NOT NULL,
	"open" decimal(8,2) NOT NULL,
	"high" decimal(8,2) NOT NULL,
	"close" decimal(8,2) NOT NULL,
	"low" decimal(8,2) NOT NULL,
	"volume" int8,
	"amount" decimal(12,2)
)
"""
class Stock(BaseModel):
    """"定义数据模型"""
    table = 't_stocks'
    __tablename__= table
    id = Column(Integer, primary_key=True, comment='自增长id')
    code = Column(VARCHAR(8), unique=True, nullable=False, comment='股票代码')
    autype = Column(VARCHAR(8), nullable=False, comment='复权类型：qfq-前复权、hfq-后复权、None-不复权，默认为qfq')
    index = Column(Boolean, nullable=False, comment='是否是大盘指数，默认为False')
    date = Column(DATE, nullable=False, comment='交易日期')
    open = Column(DECIMAL(8,2), nullable=False, comment='开盘价')
    high = Column(DECIMAL(8,2), nullable=False, comment='最高价')
    close = Column(DECIMAL(8,2), nullable=False, comment='收盘价')
    low = Column(DECIMAL(8,2), nullable=False, comment='最低价')
    volume = Column(BIGINT, nullable=True, comment='成交量')
    amount = Column(DECIMAL(12,2), nullable=True, comment='成交金额')

    def __init__(self, code, autype='qfq', index=False, date=None, open=None, high=None, close=None, low=None, volume=None, amount=None):
        self.code = code
        self.autype = autype
        self.index = index
        self.date = date
        self.open = open
        self.high = high
        self.close = close
        self.low = low
        self.volume = volume
        self.amount = amount

    # def __init__(self, code, autype):
    #     self.__init__(self, code, autype, index=False, date=None, open=None, high=None, close=None, low=None,
    #                   volume=None, amount=None)

    def __init__(self, code):
        self.code = code
        self.autype = 'qfq'
        self.index = False
        self.date = None
        self.open = None
        self.high = None
        self.close = None
        self.low = None
        self.volume = None
        self.amount = None

    def __repr__(self):
        return '<Stock %s, %s, %s, %s, %f, %f, %f, %f, %d, %f>' % (self.code, self.autype, self.index, self.date, self.open, self.high, self.close, self.low, self.volume, self.amount)
