from futu import *
import csv
import os
import time
import pandas as pd
import virtual_trade

os.chdir('HSI')

df = pd.read_csv('HK.00700.csv', parse_dates=True, index_col='update_time')
price = (df['last_price'][-1])
virtual_trade.Trade(price=price,code="HK.00700",trd_side=TrdSide.SELL)