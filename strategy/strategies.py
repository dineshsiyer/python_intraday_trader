import talib

def rsi(data, period=14):
    data['RSI'] = talib.RSI(data['Close'], timeperiod=period)
    return data

def cci(data, period=20):
    data['CCI'] = talib.CCI(data['High'], data['Low'], data['Close'], timeperiod=period)
    return data