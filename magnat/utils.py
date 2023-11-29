from requests import post
from config.settings import TOKEN
from config.settings import CHANNEL


def send_message(text: str):
    try:
        url = f'https://api.telegram.org/bot{TOKEN}/sendmessage'
        params = {
            'chat_id': f"@{CHANNEL}",
            'text': text
        }
        post(url, params=params)
    except Exception as e:
        print(f"Xato ro'y berdi: {e}")
