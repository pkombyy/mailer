# config.py
import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Настройки для smtp
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT =  os.getenv("SMTP_PORT")
EMAIL_ADDRESS= os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD= os.getenv("EMAIL_PASSWORD")
# Настройки для отправителя
FROM_EMAIL = os.getenv("FROM_EMAIL")
FROM_NAME = os.getenv("FROM_NAME")

# Токен Telegram-бота
API_TOKEN = os.getenv("API_TOKEN")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split(",")))
ALLOWED_USERS = set(map(int, os.getenv("ALLOWED_USERS", "").split(",")))