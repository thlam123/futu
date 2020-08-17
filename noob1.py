from futu import *

trd_ctx = OpenHKTradeContext(host='127.0.0.1', port=11111)

print(trd_ctx.cancel_all_order(trd_env=TrdEnv.SIMULATE))
trd_ctx.close()