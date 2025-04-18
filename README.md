# 📈 Python Trading Bot 

This is an automated trading bot built in Python that uses technical analysis to generate buy/sell signals and notify you via Telegram. The project is modular and extensible for future improvements.

---

## 🧠 Features

- Fetches historical stock data using **yfinance**
- Calculates RSI and CCI indicators using **TA-Lib**
- Generates buy/sell signals based on RSI & CCI thresholds
- Sends trade alerts to **Telegram**
- Designed with clean, scalable architecture

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/python_intraday_trader.git
cd python_intraday_trader
```
```
pip install -r requirements.txt
```
## 🛠 Dependencies
- yfinance

- pandas

- ta-lib

- requests

## ▶️ Usage
Run the bot:
```
python main.py
```
It will:

- Fetch historical data

- Apply RSI & CCI strategies

- Generate signals

- Notify you if a trade condition is met
## 📬 Telegram Notifications
To receive alerts:

- Create a Telegram bot via @BotFather

- Get your bot token and chat ID

- Add them in telegram_bot.py

## ✅ To-Do / Improvements
- Add backtesting functionality

- Add stop-loss / take-profit logic

- Integrate with broker API for auto-execution

- Add logging and error tracking

- Store trade history in a database or CSV

## 🧑‍💻 Author
Dinesh • [GitHub](https://github.com/dineshsiyer)
