from futu import *

trd_ctx = OpenHKTradeContext(host='127.0.0.1', port=11111)
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

def Trade(price,code,trd_side):
    ret, data = quote_ctx.get_stock_basicinfo(Market.HK, SecurityType.STOCK,code)
    quantity=data['lot_size']

    print(trd_ctx.place_order(price=price,qty=quantity, code=code, trd_env=TrdEnv.SIMULATE,trd_side=trd_side))

