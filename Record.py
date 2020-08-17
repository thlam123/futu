from futu import *
import csv
import pandas as pd


trd_ctx = OpenHKTradeContext(host='127.0.0.1', port=11111)
ret, data1 = trd_ctx.history_order_list_query(trd_env=TrdEnv.SIMULATE)

if ret == RET_OK:



    with open('Trade_Record.csv', 'w', newline='',encoding='utf_8_sig') as csvFile:

        headers = ['trd_side', 'order_type', 'order_status', 'order_id', 'code', 'stock_name', 'qty',
                   'price', 'create_time', 'updated_time', 'dealt_qty', 'dealt_avg_price', 'last_err_msg',
                   'remark']

        trd_side = (data1['trd_side'].values.tolist())
        order_type = (data1['order_type'].values.tolist())
        order_status = (data1['order_status'].values.tolist())
        order_id = (data1['order_id'].values.tolist())
        code = (data1['code'].values.tolist())
        stock_name = (data1['stock_name'].values.tolist())
        qty = (data1['qty'].values.tolist())
        price = (data1['price'].values.tolist())
        create_time = (data1['create_time'].values.tolist())
        updated_time = (data1['updated_time'].values.tolist())
        dealt_qty = (data1['dealt_qty'].values.tolist())
        dealt_avg_price = (data1['dealt_avg_price'].values.tolist())
        last_err_msg = (data1['last_err_msg'].values.tolist())
        remark = (data1['remark'].values.tolist())




        writer = csv.writer(csvFile)
        writer.writerow(headers)

        for i in range(len((trd_side))):
            writer.writerow([trd_side[i], order_type[i], order_status[i], order_id[i], code[i], stock_name[i], qty[i],
            price[i], create_time[i], updated_time[i], dealt_qty[i], dealt_avg_price[i], last_err_msg[i],
            remark[i]])


trd_ctx.close()