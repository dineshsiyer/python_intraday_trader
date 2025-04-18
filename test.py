import yfinance as yf
import talib as ta
import pandas as pd
import numpy as np
pd.set_option('display.max_rows',None)

data = yf.Ticker('HDFCBANK.NS').history(period='200d',interval='1d')
data['CCI'] = ta.CCI(data['High'],data['Low'],data['Close'],timeperiod=20) 
print(data)