

from alpha_vantage.timeseries import TimeSeries
from datetime import date

ts = TimeSeries(key='YRVKHQ8M0H0BWJDZ')

op = list()
cl = list()
vol = list()
t = str(date.today())

k = 0
for sym in [ 'ADBE', 'AAPL', 'MSFT', 'JPM', 'GOOGL', 'AMZN', 'ADR', 'FB']:
    d
