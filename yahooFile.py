

from yahoo_fin import stock_info as si
from datetime import date, timedelta
op = list()
cl = list()
vol = list()
t = str(date.today())


today = date.today()
yesterday = date.today() - timedelta(days=1)


# df = si.get_data('ORCL', start_date=yesterday, end_date=today)
# print(df)
# op.append((list(df['open'])[0]))
# op.append((list(df['open'])[0]))
# cl.append((list(df['adjclose'])[0]))
# vol.append((list(df['volume'])[0]))


for sym in ['AAPL', 'MSFT', 'JPM', 'GOOGL', 'AMZN', 'ADBE', 'ORCL', 'FB']:
    df = si.get_data(sym, start_date=yesterday, end_date=today)
    op.append((list(df['open'])[0]))
    cl.append((list(df['adjclose'])[0]))
    vol.append((list(df['volume'])[0]))

print(op)
print(cl)
print(vol)
# print(type(op))
# print(df[['adjclose']])
# print(df[['volume']])
