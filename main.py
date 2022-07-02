import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import dates

# read csv file using pandas 
df=pd.read_csv('data/crypto/data.csv',parse_dates=['Date'],date_parser=lambda x: pd.datetime.strptime(x,'%Y-%m-%d %I-%p'))
df.set_index('Date',inplace=True)
df.index=pd.to_datetime(df.index)
df=df.resample('1M').agg({'High':'max','Low':'min'})



# Plotting using matplotlib
formatter=dates.DateFormatter('%b-%Y')

plt.style.use('seaborn')
plt.xlabel('Year')
plt.ylabel('Price In USD')
plt.title("Etherium Price")


plt.bar(df.index,df['High'],width=12,label='Highest Price')
plt.bar(df.index,df['Low'],width=12,label="Lowest Price")

plt.gcf().autofmt_xdate()
plt.gca().xaxis.set_major_formatter(formatter)
plt.legend()

plt.tight_layout()
plt.show()