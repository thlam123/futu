from futu import *

trd_ctx = OpenHKTradeContext(host='127.0.0.1', port=11111)

print(trd_ctx.place_order(price=700,qty=100, code="HK.00700", trd_env=TrdEnv.SIMULATE,trd_side=TrdSide.BUY))
trd_ctx.close()