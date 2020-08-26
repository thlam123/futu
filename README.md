HSI Virtual Algo Trading
-



## Introduction
 - `HSI_VirtualAlgoTrade.py` record the price of HSI every 1 minutes
 - The information of the stocks would be recorded in `HSI` directory
 - If `MA5<MA20`,buy the stock
 - If `MA5>MA20`,sell the stock
 - At 15:50,sell all the stocks currently hold
 
## How to use
 - Use cmd to move to the directory futu123
 - Type the following command in cmd and the program will run automatically to trade and record
 - python HSI_VirtualAlgoTrade.py
## HSI_VirtualAlgoTrade.py
````python
#Check if the HSI directory exist.
#If not,create HSI and move to HSI.

if not os.path.exists('HSI'):
    os.makedirs('HSI')

os.chdir('HSI')
````
In the job function , we would have the following things
````python
#Create an list of HSI stocks by their code.

HSI_list = (data1['code'].values.tolist())
````
For every stock in the list,we do the following jobs
````python
for stock in HSI_list:
````

````python
#Use the Futu function "get_market_snapshot" to get the information of each stocks
#The return information would be stored in data2

ret, data2 = quote_ctx.get_market_snapshot([stock])
````


````python
#Create the csv file in HSI (HK.00001.csv)

filename = stock + ".csv"
                with open(filename, 'a', newline='') as csvFile:
#Create the headers in the CSV file

                    headers = ['update_time', 'last_price', 'volume', 'turnover', 'turnover_rate', 'ask_price',
                               'bid_price', 'ask_vol', 'bid_vol', 'avg_price', 'amplitude', 'bid_ask_ratio',
                               'volume_ratio']

                    writer = csv.writer(csvFile)
#Store the information of the stocks in the following variable

                    update_time = str(data2['update_time'].values)
                    last_price = float(data2['last_price'].values)
                    volume = float(data2['volume'].values)
                    turnover = float(data2['turnover'].values)
                    turnover_rate = float(data2['turnover_rate'].values)
                    ask_price = float(data2['ask_price'].values)
                    bid_price = float(data2['bid_price'].values)
                    ask_vol = float(data2['ask_vol'].values)
                    bid_vol = float(data2['bid_vol'].values)
                    avg_price = float(data2['avg_price'].values)
                    amplitude = float(data2['amplitude'].values)
                    bid_ask_ratio = float(data2['bid_ask_ratio'].values)
                    volume_ratio = float(data2['volume_ratio'].values)
````

````python
#Reformatting the update time(exclude the brackets)
                    
                    new_update_time = ""

                    for i in range(len(update_time)):
                        if (i != 0) and (i != 1) and (i != 21) and (i != 22):
                            new_update_time = new_update_time + update_time[i]
````
````python
#Check if size of file is 0.If not,write the headers

                    if os.stat(filename).st_size == 0:
                        writer.writerow(headers)
````

````python
#Write the information of the stocks in the csv file

                    writer.writerow(
                        [new_update_time, last_price, volume, turnover, turnover_rate, ask_price, bid_price, ask_vol,
                         bid_vol, avg_price, amplitude, bid_ask_ratio, volume_ratio])
````
Create a data frame to calculate the MA
```python
#Create a data frame df
#Add 3 column: MA5 , MA20  , MA diff
#Convert the df to CSV

                df = pd.read_csv(filename, parse_dates=True, index_col='update_time')
                price = (df['last_price'])
                df['MA5'] = price.rolling(window=5).mean()
                df['MA20'] = price.rolling(window=20).mean()
                df['MA diff'] = df['MA5'] - df['MA20']
                new_df = df.drop_duplicates()
                final_df=new_df.reset_index()
                final_df.to_csv(filename, index=0)
````

````python
#Move to the parent directory (futu123)
                os.chdir('..')
````

Since futu virtual envirnonment could only place order of 15 stocks every 30 seconds , we
only trade the 15 stocks with highest MA diff
````python
#Create a temporary csv file BestMa.csv

                with open("BestMa.csv", 'a', newline='') as csvFile:
                    headers2 =['Code','last_price','MA diff', 'Abs MA diff']
                    writer2 = csv.writer(csvFile)

#Write the headers of the BestMa.csv

                    if os.stat("BestMa.csv").st_size == 0:
                        writer2.writerow(headers2)

#Write the stock code, last price , current MA diff , absolute value MA diff
#Sort df2 by the MA diff


                    writer2.writerow(
                        [stock, price[-1], new_df['MA diff'][-1], abs(new_df['MA diff'][-1])])
                df2 = pd.read_csv("BestMa.csv")
                Sorted_df2=df2.sort_values(by ='Abs MA diff', ascending=False)

#Go back to the parent directory(HSI) to write the next stock

                os.chdir('HSI')
                
````

After finishing the for loop, the df2 now would contain the absolute difference of all HSI stocks. 
The df2 is sorted by the absolute difference

````python
#Take the 15 stocks with the highest value of absolute value of MA diff

        Final_df2=Sorted_df2.head(15)
        Ult_df2=Final_df2.reset_index()
````

````python
#BUY or SELL each stocks in the best 15 MA diff dataframe
#Pass the value to the function Trade() in virtual_trade
#Quantity is fixed as 1 lot in the function Trade()

        for ind in Ult_df2.index:
            if (Ult_df2['MA diff'][ind] > 0):
                virtual_trade.Trade(price=Ult_df2['last_price'][ind], code=Ult_df2['Code'][ind], trd_side=TrdSide.BUY)
            elif (Ult_df2['MA diff'][ind] < 0):
                virtual_trade.Trade(price=Ult_df2['last_price'][ind], code=Ult_df2['Code'][ind], trd_side=TrdSide.SELL)
````
````python

#Go back to the parent directory(futu123)
#Remove the temporary file(BestMa.csv)
#Go to HSI, ready for the next job() after 1 minute
#结束job()后记得关闭当条连接，防止连接条数用尽
        os.chdir('..')
        os.remove("BestMa.csv")
        os.chdir('HSI')
     quote_ctx.close()
````
Then we set the time loop for the program
````python
while True:
    obj_now = datetime.now()
#Trading hours would be 9 10 11 13 14 15,loop job() every 1 minute

    if (obj_now.hour == 9) or (obj_now.hour == 10) or (obj_now.hour == 11) or (obj_now.hour == 13) or (
            obj_now.hour == 14) or (obj_now.hour == 15):

        if (obj_now.hour == 15) and ((obj_now.minute == 50) or (obj_now.minute == 51) or (obj_now.minute == 52)
        or (obj_now.minute == 53) or (obj_now.minute == 54) or (obj_now.minute == 55)
        or (obj_now.minute == 56) or (obj_now.minute == 57) or (obj_now.minute == 58)
        or (obj_now.minute == 59)):
            foldername = os.path.basename(os.getcwd())

            if (foldername == "HSI"):
                os.chdir('..')

#At 15:50,run the Virtual_SellAllStock.py in terminal to sell all the stocks

            os.system("python Virtual_SellAllStock.py")
            print(os.getcwd())
            time.sleep(30)
            continue



        job()

    time.sleep(60)
````

## virtual_trade.py

!! The quantity of the stocks could be adjusted !!\
!! The default is 1 lot                         !!

````python
from futu import *

trd_ctx = OpenHKTradeContext(host='127.0.0.1', port=11111)
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)

#Use the "trd_ctx.place_order" function to trade

def Trade(price,code,trd_side):

#Get the lot size(每手) of the stocks we want to trade 
#If you want to trade more lots at each order, just add a multiplier in front of the quantity (eg:3*quantity)

    ret, data = quote_ctx.get_stock_basicinfo(Market.HK, SecurityType.STOCK,code)
    quantity=data['lot_size']

    print(trd_ctx.place_order(price=price,qty=quantity, code=code, trd_env=TrdEnv.SIMULATE,trd_side=trd_side))
````

## Virtual_SellAllStock.py




