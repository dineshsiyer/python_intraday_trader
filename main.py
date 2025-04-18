from config.constants import NIFTY_50
import python_intraday_trader.utils.fetch_data as fetch_data
import python_intraday_trader.strategy.strategies as st
import python_intraday_trader.utils.trades as td


def check_signal(result):
    if not result:
        return 'none'  # or return None if you prefer

    signal = result.get('signal')

    if signal == 'buy':
        return 'buy' 
    elif signal == 'sell':
        return 'sell' 
    else:
        return 'none'

    
def take_trade(signal, symbol, price):
    if signal == 'buy':
        td.trade(check='buy', symbol=symbol, price=price)
        return
    elif signal == 'sell':
        td.trade(check='sell', symbol=symbol, price=price)
        return
    else:
        return

def main():
    for ticker in NIFTY_50:  
        data = fetch_data.get_data(ticker,period='200d', interval='1d')
        data = st.rsi(data)
        data = st.cci(data)
        data = td.generate_rsi_cci_signals(data)
        result = td.check_for_trade(data)
        bool = check_signal(result=result)
        # print(bool)
        if bool!='none':
            take_trade(signal=bool, symbol=ticker, price=result.get('price'))
    return
        
if __name__ == '__main__':
    main()