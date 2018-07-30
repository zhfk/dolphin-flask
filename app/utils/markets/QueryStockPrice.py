import tushare as ts
from app.model.Stock import Stock
import datetime
from io import StringIO
from app.utils.database.Connect import *

# df = ts.get_stock_basics()

# 此逻辑有缺陷，最新的行情日期在收盘前是昨日，收盘后是今日
# 获得指定股票代码的最新的行情价格
def get_period_close(code, start, end):
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

# 获得昨日的日期
def get_yesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    return yesterday

# 获得期间工作日
def get_weekday(start, end):
    begin_date = datetime.datetime.strptime(start, "%Y-%m-%d")
    stop_date = datetime.datetime.strptime(end, "%Y-%m-%d")
    date_generated = [begin_date + datetime.timedelta(days=x) for x in range(0, (stop_date - begin_date).days)]
    weekday = []
    for date in date_generated:
        if date.weekday() < 5:
            weekday.append(date)
    return weekday

if __name__ == '__main__':
    # print(str(get_yesterday()))
    # get_period_close('000001', '2018-07-01', get_yesterday())
    get_weekday("2018-07-23", "2018-08-04")