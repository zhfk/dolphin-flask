import tushare as ts
from app.model.Stock import Stock
import datetime
from io import StringIO
from flask import request

# df = ts.get_stock_basics()


def get_last_close(code, start, end):
    # print("stock's code is ", stock.code)
    df = ts.get_h_data(code, start=str(start), end=str(end))
    print(df.head(1))
    # stock.open = last_one['open']
    # stock.high = last_one['high']
    # stock.close = last_one['close']
    # stock.low = last_one['low']
    # stock.volume = last_one['volume']
    # stock.amount = last_one['amount']
    # print(stock)
    buf = StringIO()
    df.to_csv(buf, na_rep='None')
    print(buf.getvalue())
    return buf.getvalue()

def get_yesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday

# if __name__ == '__main__':
#     stock = Stock(code = '002337')
#     QueryStock.get_last_close(stock, '2018-07-01', get_yesterday())