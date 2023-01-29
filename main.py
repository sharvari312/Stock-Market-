import requests
from datetime import datetime
import time
import pandas as pd

ticker = input("Enter the ticker symbol: ")
from_date = input('Enter start date in yyyy/mm/dd format:')
to_date = input('Enter end date in yyyy/mm/dd format:')

from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))


url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content = requests.get(url, headers=headers).content


with open('data.csv', 'wb') as file:
  file.write(content)
  file.close()

df=pd.read_csv('data.csv')

#index_labels=[0,1]
df2=pd.DataFrame(df.query('Close == Close.max()'))
print(df2)
df2=df2.append(df.query('Close == Close.min()'), ignore_index=True)
print(df2)
print(f"Maximum closing value {df2.Close[0]} is for date {df2.Date[0]} ")
print(f"Minimum closing value {df2.Close[1]} is for date {df2.Date[1]}")


