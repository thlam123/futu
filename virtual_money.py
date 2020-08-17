from futu import *

trd_ctx = OpenHKTradeContext(host='127.0.0.1', port=11111)

print(trd_ctx.accinfo_query(trd_env=TrdEnv.SIMULATE))
trd_ctx.close()