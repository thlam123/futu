from futu import *
import os
import pandas as pd

trd_ctx = OpenHKTradeContext(host='127.0.0.1', port=11111)



os.chdir('HSI')
path = os.getcwd()
myFiles=os.listdir(path)

for f in myFiles:
    data = pd.read_csv(f, parse_dates="update_time", index_col='update_time')
    price = (data['last_price'])


trd_ctx.close()





print(trd_ctx.place_order(price=700.0, qty=100, code="HK.00700", trd_env=TrdEnv.SIMULATE,trd_side=TrdSide.BUY))