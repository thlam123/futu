from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
import csv
import os



style.use('ggplot')

Analysis="/Users/lamtikhei/PycharmProjects/futu123/HSI/HK.00700.csv"

data=pd.read_csv(Analysis,parse_dates=True,index_col='update_time')
price=(data['last_price'])


mov_avg=price.rolling(20).mean()

plt.plot(price,color='b')
plt.plot(mov_avg,color='r')

plt.show()