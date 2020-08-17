from futu import *
import os
import pandas as pd





os.chdir('HSI')
path = os.getcwd()
myFiles=os.listdir(path)



df = pd.read_csv('HK.00700.csv', parse_dates=True, index_col='update_time')
price = (df['last_price'])

df['MA5'] = price.rolling(window=5).mean()
df['MA20'] = price.rolling(window=20).mean()
df['MA diff']=df['MA5']-df['MA20']
print(df['MA diff'][-1])
print(df)








