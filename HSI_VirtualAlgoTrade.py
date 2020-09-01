from futu import *
import csv
import os
import time
import pandas as pd
import virtual_trade


from datetime import datetime

if not os.path.exists('HSI'):
    os.makedirs('HSI')

os.chdir('HSI')


def job():
    quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
    ret, data1 = quote_ctx.get_plate_stock('HK.HSI Constituent')

    if ret == RET_OK:
        HSI_list = (data1['code'].values.tolist())  # 恆指成份股list
        for stock in HSI_list:


            ret, data2 = quote_ctx.get_market_snapshot([stock])
            if ret == RET_OK:
                filename = stock + ".csv"
                with open(filename, 'a', newline='') as csvFile:
                    headers = ['update_time', 'last_price', 'volume', 'turnover', 'turnover_rate', 'ask_price',
                               'bid_price', 'ask_vol', 'bid_vol', 'avg_price', 'amplitude', 'bid_ask_ratio',
                               'volume_ratio']

                    writer = csv.writer(csvFile)

                    update_time = str(data2['update_time'].values)
                    last_price = (data2['last_price'].values[0])
                    volume = (data2['volume'].values[0])
                    turnover = (data2['turnover'].values[0])
                    turnover_rate = (data2['turnover_rate'].values[0])
                    ask_price = (data2['ask_price'].values[0])
                    bid_price = (data2['bid_price'].values[0])
                    ask_vol = (data2['ask_vol'].values[0])
                    bid_vol = (data2['bid_vol'].values[0])
                    avg_price = (data2['avg_price'].values[0])
                    amplitude = (data2['amplitude'].values[0])
                    bid_ask_ratio = (data2['bid_ask_ratio'].values[0])
                    volume_ratio = (data2['volume_ratio'].values[0])

                    new_update_time = ""

                    for i in range(len(update_time)):
                        if (i != 0) and (i != 1) and (i != 21) and (i != 22):
                            new_update_time = new_update_time + update_time[i]

                    # check if size of file is 0
                    if os.stat(filename).st_size == 0:
                        writer.writerow(headers)

                    writer.writerow(
                        [new_update_time, last_price, volume, turnover, turnover_rate, ask_price, bid_price, ask_vol,
                         bid_vol, avg_price, amplitude, bid_ask_ratio, volume_ratio])

                df = pd.read_csv(filename, parse_dates=True, index_col='update_time')
                print(df)
                price = (df['last_price'])
                df['MA5'] = price.rolling(window=5).mean()
                df['MA20'] = price.rolling(window=20).mean()
                df['MA diff'] = df['MA5'] - df['MA20']
                new_df = df.drop_duplicates()
                final_df=new_df.reset_index()
                final_df.to_csv(filename, index=0)

                os.chdir('..')

                with open("BestMa.csv", 'a', newline='') as csvFile:
                    headers2 =['Code','last_price','MA diff', 'Abs MA diff']
                    writer2 = csv.writer(csvFile)
                    if os.stat("BestMa.csv").st_size == 0:
                        writer2.writerow(headers2)
                    writer2.writerow(
                        [stock, price[-1], new_df['MA diff'][-1], abs(new_df['MA diff'][-1])])
                df2 = pd.read_csv("BestMa.csv")
                Sorted_df2=df2.sort_values(by ='Abs MA diff', ascending=False)
                os.chdir('HSI')


        Final_df2=Sorted_df2.head(15)
        Ult_df2=Final_df2.reset_index()
        for ind in Ult_df2.index:
            if (Ult_df2['MA diff'][ind] > 0):
                virtual_trade.Trade(price=Ult_df2['last_price'][ind], code=Ult_df2['Code'][ind], trd_side=TrdSide.BUY)
            elif (Ult_df2['MA diff'][ind] < 0):
                virtual_trade.Trade(price=Ult_df2['last_price'][ind], code=Ult_df2['Code'][ind], trd_side=TrdSide.SELL)

        os.chdir('..')
        os.remove("BestMa.csv")
        os.chdir('HSI')






    quote_ctx.close()  # 结束后记得关闭当条连接，防止连接条数用尽


while True:
    obj_now = datetime.now()
    if (obj_now.hour == 9) or (obj_now.hour == 10) or (obj_now.hour == 11) or (obj_now.hour == 13) or (
            obj_now.hour == 14) or (obj_now.hour == 15):

        if (obj_now.hour == 15) and ((obj_now.minute == 50) or (obj_now.minute == 51) or (obj_now.minute == 52)
        or (obj_now.minute == 53) or (obj_now.minute == 54) or (obj_now.minute == 55)
        or (obj_now.minute == 56) or (obj_now.minute == 57) or (obj_now.minute == 58)
        or (obj_now.minute == 59)):
            foldername = os.path.basename(os.getcwd())

            if (foldername == "HSI"):
                os.chdir('..')
            os.system("python Virtual_SellAllStock.py")
            print(os.getcwd())
            time.sleep(30)
            continue



        job()

    time.sleep(60)
