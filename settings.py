import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
USERS_TO_PING = os.getenv('USERS_TO_PING')
