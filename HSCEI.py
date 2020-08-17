from futu import *
import csv
import os
import time
import pandas as pd


from datetime import datetime

if not os.path.exists('HSCEI'):
    os.makedirs('HSCEI')

os.chdir('HSCEI')


def job():
    quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
    ret, data1 = quote_ctx.get_plate_stock('HK.HSCEI Stock')

    if ret == RET_OK:
        HSCEI_list = (data1['code'].values.tolist())  # 恆指成份股list
        for stock in HSCEI_list:

            ret, data2 = quote_ctx.get_market_snapshot([stock])
            if ret == RET_OK:
                filename = stock + ".csv"
                with open(filename, 'a', newline='') as csvFile:
                    headers = ['update_time', 'last_price', 'volume','turnover','turnover_rate','ask_price','bid_price','ask_vol','bid_vol','avg_price','amplitude','bid_ask_ratio','volume_ratio']

                    writer = csv.writer(csvFile)



                    update_time = str(data2['update_time'].values)
                    last_price = float(data2['last_price'].values)
                    volume = float(data2['volume'].values)
                    turnover = float(data2['turnover'].values)
                    turnover_rate = float(data2['turnover_rate'].values)
                    ask_price = float(data2['ask_price'].values)
                    bid_price = float(data2['bid_price'].values)
                    ask_vol = float(data2['ask_vol'].values)
                    bid_vol = float(data2['bid_vol'].values)
                    avg_price = float(data2['avg_price'].values)
                    amplitude = float(data2['amplitude'].values)
                    bid_ask_ratio = float(data2['bid_ask_ratio'].values)
                    volume_ratio = float(data2['volume_ratio'].values)


                    new_update_time = ""

                    for i in range(len(update_time)):
                        if (i != 0) and (i != 1) and (i != 21) and (i != 22):
                            new_update_time = new_update_time + update_time[i]


                    # check if size of file is 0
                    if os.stat(filename).st_size == 0:
                        writer.writerow(headers)

                    writer.writerow([new_update_time, last_price,volume,turnover,turnover_rate,ask_price,bid_price,ask_vol,bid_vol,avg_price,amplitude,bid_ask_ratio,volume_ratio])

                df = pd.read_csv(filename)
                new_df=df.drop_duplicates()
                new_df.to_csv(filename, index=0)

            else:
                print('error:', data2)





    else:
        print('error:', data1)
    quote_ctx.close()  # 结束后记得关闭当条连接，防止连接条数用尽

while True:
    obj_now = datetime.now()
    if (obj_now.hour==9) or (obj_now.hour==10) or (obj_now.hour==11) or (obj_now.hour==13) or (obj_now.hour==14) or (obj_now.hour==15):
        job()
    time.sleep(60)