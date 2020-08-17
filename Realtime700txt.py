from futu import *
import schedule
import time
def job():
    quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
    ret, data = quote_ctx.get_market_snapshot(['HK.00700'])
    if ret == RET_OK:
        sys.stdout = open("00700.txt", "a")

        print(data['update_time'].values,data['last_price'].values)    # 转为list

    else:
        print('error:', data)
    quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽

while True:
    job()
    time.sleep(60)

