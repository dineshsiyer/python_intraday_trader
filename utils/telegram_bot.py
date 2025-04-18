import requests
from config.constants import TELEGRAM_TOKEN,CHAT_ID


TOKEN = TELEGRAM_TOKEN
CHAT_ID = CHAT_ID

def push_notification(message="Hello from my Python bot!"):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        params = {
            "chat_id": CHAT_ID,
            "text": message
        }

        response = requests.get(url, params=params, timeout=10)  # 10s timeout
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx/5xx)

        data = response.json()
        if not data.get("ok"):
            print(f"Telegram API Error: {data}")
        else:
            print("Message sent successfully!")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Request Error: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# push_notification('hello, Dinesh')
