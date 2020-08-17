from futu import *
import csv


trd_ctx = OpenHKTradeContext(host='127.0.0.1', port=11111)
ret, data1 = trd_ctx.position_list_query(trd_env=TrdEnv.SIMULATE)


if ret == RET_OK:



    with open('Holding_Stock_information.csv', 'w', newline='',encoding='utf_8_sig') as csvFile:

        headers = ['Position_side', 'Code', 'Stock_Name', 'Quantity', 'Can_sell_qty', 'Nominal_price', 'Cost_price',
                   'Cost_price_valid', 'Market_val', 'pl_ratio', 'pl_ratio_valid', 'pl_val', 'pl_val_valid',
                   'Today_pl_val', 'Today_buy_qty', 'Today_buy_val', 'Today_sell_qty', 'Today_sell_val','Unrealized_pl',
                   'Realized_pl']

        position_side = (data1['position_side'].values.tolist())
        code = (data1['code'].values.tolist())
        stock_name = (data1['stock_name'].values.tolist())
        qty = (data1['qty'].values.tolist())
        can_sell_qty = (data1['can_sell_qty'].values.tolist())
        nominal_price = (data1['nominal_price'].values.tolist())
        cost_price = (data1['cost_price'].values.tolist())
        cost_price_valid = (data1['cost_price_valid'].values.tolist())
        market_val = (data1['market_val'].values.tolist())
        pl_ratio = (data1['pl_ratio'].values.tolist())
        pl_ratio_valid = (data1['pl_ratio_valid'].values.tolist())
        pl_val = (data1['pl_val'].values.tolist())
        pl_val_valid = (data1['pl_val_valid'].values.tolist())
        today_pl_val = (data1['today_pl_val'].values.tolist())
        today_buy_qty = (data1['today_buy_qty'].values.tolist())
        today_buy_val = (data1['today_buy_val'].values.tolist())
        today_sell_qty = (data1['today_sell_qty'].values.tolist())
        today_sell_val = (data1['today_sell_val'].values.tolist())
        unrealized_pl = (data1['unrealized_pl'].values.tolist())
        realized_pl = (data1['realized_pl'].values.tolist())




        writer = csv.writer(csvFile)
        writer.writerow(headers)
        for i in range(len((position_side))):
            writer.writerow([position_side[i], code[i], stock_name[i], qty[i], can_sell_qty[i], nominal_price[i], cost_price[i],
                             cost_price_valid[i], market_val[i], pl_ratio[i], pl_ratio_valid[i], pl_val[i], pl_val_valid[i],
                             today_pl_val[i], today_buy_qty[i], today_buy_val[i], today_sell_qty[i], today_sell_val[i], unrealized_pl[i],
                             realized_pl[i]])

trd_ctx.close()