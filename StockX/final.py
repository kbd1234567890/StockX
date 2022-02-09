import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv('apple.csv')
df['Date'] = pd.to_datetime(df.Date,format='%d-%m-%Y')

data = df.sort_index(ascending=True, axis=0)
df.index = df['Date']

for i in range(0,len(data)):
    new_data['Date'][i] = data['Date'][i]
    new_data['Close'][i] = data['Close'][i]

new_data['Date'] = pd.to_datetime(new_data['Date'])
new_data['Date']=new_data['Date'].map(dt.datetime.toordinal)

model = LinearRegression()
model.fit(new_data['Date'].values.reshape(-1, 1),new_data['Close'])

df2 = pd.read_csv('demo.csv')
df2['Date'] = pd.to_datetime(df2.Date,format='%d-%m-%Y')
df2['Date'] = pd.to_datetime(df2['Date'])
df2['Date']=df2['Date'].map(dt.datetime.toordinal)
preds = model.predict(df2['Date'].values.reshape(-1, 1))

df3 = pd.read_csv('demo.csv')
df3['Date'] = pd.to_datetime(df3.Date,format='%d-%m-%Y')

plt.plot(df3, preds)



