from django.shortcuts import render
###############################
from yahoo_fin import stock_info as si
import numpy as np
from datetime import date, timedelta
import pandas as pd
import datetime as dt
from sklearn.linear_model import LinearRegression
import math
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

# from . import xx

op = list()
cl = list()
vol = list()
f_list = []
interval = ''
k = 0
companyName = ''
names = ['Apple', 'Microsoft', 'Goldman', 'Google', 'Amazon', 'Adobe', 'Oracle', 'Facebook']
symbol=["fa fa-apple", "fa fa-windows", "fa fa-glide", "fa fa-google", "fa fa-amazon", "fa fa-adn",
        "fa fa-opera", "fa fa-facebook-official"]
underline1 = ''
underline2 = ''
underline3 = ''
underline4 = ''
underline5 = 'border-bottom: solid'
graphType = 'Week'

def ker(csv_name):
    df = pd.read_csv(csv_name)
    df['timestamp'] = pd.to_datetime(df.timestamp, format='%Y-%m-%d')
    df.index = df['timestamp']
    data = df.sort_index(ascending=True, axis=0)
    new_data = pd.DataFrame(index=range(0,len(df)),columns=['Date', 'Close'])
    for i in range(0,len(data)):
        new_data['Date'][i] = data['timestamp'][i]
        new_data['Close'][i] = data['close'][i]
    new_data.index = new_data.Date
    new_data.drop('Date', axis=1, inplace=True)
    dataset = new_data.values
    train = dataset[0:len(new_data),:]
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(dataset)
    x_train, y_train = [], []
    for i in range(60,len(train)):
        x_train.append(scaled_data[i-60:i,0])
        y_train.append(scaled_data[i,0])

    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0],x_train.shape[1],1))
    # create and fit the LSTM network
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1],1)))
    model.add(LSTM(units=50))
    model.add(Dense(1))

    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(x_train, y_train, epochs=1, batch_size=1, verbose=2)
    inputs = new_data[len(new_data) - 60:len(new_data)].values
    inputs = inputs.reshape(-1,1)
    inputs  = scaler.transform(inputs)
    X_test = []
    X_test.append(inputs[0:60, 0])
    X_test = np.array(X_test)
    X_test = np.reshape(X_test, (1,X_test.shape[1],1))
    closing_price = model.predict(X_test)
    closing_price = scaler.inverse_transform(closing_price)
    print(new_data)
    print(closing_price)
    return closing_price

names = ['Apple', 'Microsoft', 'Goldman', 'Google', 'Amazon', 'Adobe', 'Oracle', 'Facebook']

Apple1 = ker('daily_Apple.csv')
Google1 = ker('daily_Google.csv')
Oracle1 = ker('daily_Oracle.csv')
Goldman1 = ker('daily_Goldman.csv')
Mocrosoft1 = ker('daily_Microsoft.csv')
Amazon1 = ker('daily_Amazon.csv')
Adobe1 = ker('daily_Adobe.csv')
Facebook1 = ker('daily_Facebook.csv')

pred_list1 = [Apple1, Mocrosoft1, Goldman1, Google1, Amazon1, Adobe1, Oracle1, Facebook1]

pred_list2 = [Apple1, Mocrosoft1, Goldman1, Google1, Amazon1, Adobe1, Oracle1, Facebook1]

pred_list3 = [Apple1, Mocrosoft1, Goldman1, Google1, Amazon1, Adobe1, Oracle1, Facebook1]



def regular(csv_name):

    df = pd.read_csv(csv_name)
    data = df.sort_index(ascending=False, axis=0)
    final_list = []
    dc1 = data['timestamp']
    dc2 = data['close']
    dc1_list = list(dc1)
    print(dc1_list)
    final_list.append(dc1_list)
    dc2_list = list(dc2)
    print(dc2_list)
    final_list.append(dc2_list)
    return final_list


def liveStock():
    global maxStock, maxStockCompany, names
    today = date.today()
    yesterday = date.today() - timedelta(days=1)
    i = 0
    names = ['Apple', 'Microsoft', 'Goldman', 'Google', 'Amazon', 'Adobe', 'Oracle', 'Facebook']
    for sym in ['AAPL', 'MSFT', 'GS', 'GOOGL', 'AMZN', 'ADBE', 'ORCL', 'FB']:
        df = si.get_data(sym, start_date=yesterday, end_date=today)
        op.append(round(list(df['open'])[0], 2))
        cl.append(round(list(df['adjclose'])[0], 2))
        vol.append((list(df['volume'])[0]))

    ind1 = cl.index(max(cl))
    maxStock = max(cl)
    maxStockCompany = names[ind1]


def dashboard(request):
    # f_list = []
    global k, f_list, companyName, pred, interval, underline5, underline4, underline3, underline2, underline1
    global graphType,symbol

    # f_list = list()
    if k == 0:
        liveStock()
        companyName = maxStockCompany
        interval = 'tom'
        pred = pred_list1[names.index(companyName)]
        f_list = regular('daily_' + companyName+'.csv').copy()
        k = k + 1
        graphType = 'Days'

    if request.POST.get('company') in ["Apple", "Microsoft", "Goldman", "Google", "Amazon", "Oracle", "Adobe",
                                       "Facebook"]:
        companyName = request.POST.get('company')
        interval = 'tom'
        pred = pred_list1[names.index(companyName)]
        f_list = regular('daily_' + companyName + '.csv').copy()
        underline5 = 'border-bottom: solid'
        underline2 = underline3 = underline1 = underline4 = ''
        graphType = 'Days'

    if isinstance(request.POST.get('1 day'), str):
        if request.POST.get('1 day') in '1 day':
            interval = 'tom'
            companyName = request.POST.get('dashCompany')
            pred = pred_list1[names.index(companyName)]
            f_list = regular('daily_' + companyName + '.csv').copy()
            underline1 = 'border-bottom: solid'
            underline2 = underline3 = underline5 = underline4 = ''
            graphType = 'Days'

    return render(request, 'dashboard.html', {'currentStock': cl[names.index(companyName)], 'x': f_list[0],
                                              'y': round(pred[0][0], 2),
                                                'z': f_list[1], 'companyName': companyName, 'maxStock': maxStock,
                                                'maxStockCompany': maxStockCompany, 'sp': cl, 'interval': interval,
                                                'underline1': underline1, 'underline2': underline2,
                                              'underline3': underline3,
                                              'underline4': underline4, 'underline5': underline5,
                                              'graphType': graphType, 'symbol': symbol[names.index(companyName)]
                                              })


def about(request):

    return render(request, 'user.html')


def document(request):

    return render(request, 'document.html')


def companyList(request):

    # op = [1, 2, 3, 4, 5, 6, 7, 8]
    # cl = [1, 2, 3, 4, 5, 6, 7, 8]
    # vol = [1, 2, 3, 4, 5, 6, 7, 8]
    return render(request, 'tables.html', {'close': cl, 'open': op, 'revenue':vol})
