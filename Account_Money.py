from futu import *
import csv


trd_ctx = OpenHKTradeContext(host='127.0.0.1', port=11111)
ret, data1 = trd_ctx.accinfo_query(trd_env=TrdEnv.SIMULATE)

if ret == RET_OK:



    with open('Money.csv', 'w', newline='',encoding='utf_8_sig') as csvFile:

        headers = ['power', 'total_assets', 'cash', 'market_val', 'frozen_cash', 'avl_withdrawal_cash', 'currency',
                   'available_funds', 'unrealized_pl', 'realized_pl', 'risk_level', 'initial_margin',
                   'maintenance_margin','hk_cash','hk_avl_withdrawal_cash','us_cash','us_avl_withdrawal_cash'
                   ]

        power = (data1['power'].values.tolist())
        total_assets = (data1['total_assets'].values.tolist())
        cash = (data1['cash'].values.tolist())
        market_val = (data1['market_val'].values.tolist())
        frozen_cash = (data1['frozen_cash'].values.tolist())
        avl_withdrawal_cash = (data1['avl_withdrawal_cash'].values.tolist())
        currency = (data1['currency'].values.tolist())
        available_funds = (data1['available_funds'].values.tolist())
        unrealized_pl = (data1['unrealized_pl'].values.tolist())
        realized_pl = (data1['realized_pl'].values.tolist())
        risk_level = (data1['risk_level'].values.tolist())
        initial_margin = (data1['initial_margin'].values.tolist())
        maintenance_margin = (data1['maintenance_margin'].values.tolist())
        hk_cash = (data1['hk_cash'].values.tolist())
        hk_avl_withdrawal_cash = (data1['hk_avl_withdrawal_cash'].values.tolist())
        us_cash = (data1['us_cash'].values.tolist())
        us_avl_withdrawal_cash = (data1['us_avl_withdrawal_cash'].values.tolist())




        writer = csv.writer(csvFile)
        writer.writerow(headers)
        for i in range(len((power))):
            writer.writerow([power[i], total_assets[i], cash[i], market_val[i], frozen_cash[i], avl_withdrawal_cash[i], currency[i],
                             available_funds[i], unrealized_pl[i], realized_pl[i], risk_level[i], initial_margin[i],
                             maintenance_margin[i],hk_cash[i],hk_avl_withdrawal_cash[i],us_cash[i],us_avl_withdrawal_cash[i]
                             ])

trd_ctx.close()