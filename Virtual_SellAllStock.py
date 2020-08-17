from futu import *
import os
import pandas as pd




def Trade(price, code,qty):
    trd_ctx = OpenHKTradeContext(host='127.0.0.1', port=11111)
    print(trd_ctx.place_order(price=price, qty=qty, code=code, trd_env=TrdEnv.SIMULATE, trd_side=TrdSide.SELL))
    trd_ctx.close()



os.system("python Holding_Stock_info.py")

with open("Holding_Stock_information.csv", 'r', newline='') as csvFile:
    df = pd.read_csv("Holding_Stock_information.csv")
    Code_list=df['Code']
    Price_list=df['Nominal_price']
    Qty_list=df['Can_sell_qty']
    Profit_list=df['Nominal_price']-df['Cost_price']

    for i in range(len(Code_list)):
        Trade(Price_list[i],Code_list[i],Qty_list[i])





