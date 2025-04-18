import yfinance as yf

def get_data(ticker,period='1d', interval='1d'):
    data = yf.Ticker(ticker=ticker).history(period=period, interval=interval)
    return data