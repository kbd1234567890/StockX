import numpy as np
from datetime import date, timedelta
import pandas as pd
import datetime as dt
from sklearn.linear_model import LinearRegression
import math
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM

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
ker('daily_AAPL.csv')