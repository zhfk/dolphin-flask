import tushare as ts
from app.model.Stock import Stock
import datetime
from io import StringIO
from app.utils.database.Connect import *

# df = ts.get_stock_basics()

def get_last_close(code, start, end):
    # print("stock's code is ", stock.code)
    df = ts.get_h_data(code, start=str(start), end=str(end))
    # print(df.head(1))
    # db_session = get_session()
    # for index, row in df.iterrows():
    #     # row = df.loc[index].values[0:-1]
    #     # print(index, row)
    #     stock = Stock(code)
    #     stock.date = index
    #     stock.open = row['open']
    #     stock.high = row['high']
    #     stock.close = row['close']
    #     stock.low = row['low']
    #     stock.volume = row['volume']
    #     stock.amount = row['amount']
    #     print(stock)
    #     add_stock_info(stock, db_session)

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