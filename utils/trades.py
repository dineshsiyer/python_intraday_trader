import python_intraday_trader.utils.telegram_bot as telegram_bot
import pandas as pd

def generate_rsi_cci_signals(data):
    data['Signals'] = pd.Series('', index=data.index, dtype='object')
    data.loc[
        (data['RSI'] < 30) &
        (data['CCI'] < -100),
        'Signals'
    ] = 'buy'

    data.loc[
        (data['RSI'] > 70) &
        (data['CCI'] > 100),
        'Signals'
    ] = 'sell'
    return data

def check_for_trade(data):
    # print(data.iloc[-1])
    if data['Signals'].iloc[-1] == 'buy':
        return {'signal':'buy', 'price':round(data['Close'].iloc[-1],2)}
    elif data['Signals'].iloc[-1] == 'sell':
        return {'signal':'sell', 'price':round(data['Close'].iloc[-1],2)}
    else:
        return

def trade(check, symbol, price):
    if symbol == "" or check == '' or price == '':

        return
    else:
        message = f'{check} {symbol} at {price}'
        print(message)
        telegram_bot.push_notification(message=message)