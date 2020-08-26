from futu import *
import csv
import time
def job():
    quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
    ret, data = quote_ctx.get_market_snapshot(['HK.00700'])
    if ret == RET_OK:
        with open('00700.csv', 'a', newline='') as csvFile:
            writer = csv.writer(csvFile)
            update_time = str(data['update_time'].values)
            last_price = float(data['last_price'].values)

            new_update_time = ""

            for i in range(len(update_time)):
                if (i != 0) and (i != 1) and (i != 21) and (i != 22):
                    new_update_time = new_update_time + update_time[i]

            writer.writerow([new_update_time, last_price])

    else:
        print('error:', data)
    quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽

while True:
    job()
    time.sleep(60)
    #diu