import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.fsm.storage.memory import MemoryStorage
from db import connect_db, create_tables
from config import  API_TOKEN, ALLOWED_USERS
from handlers import  start_router, admin_router, email_router

# Настройки логирования
logging.basicConfig(level=logging.INFO)

# Проверка токена
if not API_TOKEN:
    raise ValueError("Отсутствует API_TOKEN в .env файле!")
 

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Подключение роутеров
dp.include_routers(start_router,admin_router,email_router)
# Подключение к базе данных
db_connection = connect_db()  # Синхронное подключение
create_tables(db_connection)  # Синхронное создание таблиц

# Глобальная переменная для отслеживания состояния бота
bot_is_running = False


async def notify_users(message: str):
    """Уведомление пользователей о состоянии бота."""
    for user_id in ALLOWED_USERS:
        try:
            await bot.send_message(user_id, message)
        except Exception as e:
            logging.error(f"Не удалось отправить сообщение пользователю {user_id}: {e}")


async def on_startup():
    """Действия при запуске бота."""
    global bot_is_running
    bot_is_running = True
    await notify_users("Бот запущен и готов к работе!")
    logging.info("Бот запущен и готов к работе!")


async def on_shutdown():
    """Действия при остановке бота."""
    global bot_is_running
    bot_is_running = False
    await notify_users("Бот остановлен. Все запросы будут проигнорированы.")
    logging.info("Бот остановлен.")


async def main():
    """Основной цикл бота."""
    try:
        # Логирование успешного старта
        logging.info("Запуск бота...")
        await on_startup()
        # Запуск опроса
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Критическая ошибка: {e}")
    finally:
        # Действия при остановке
        await on_shutdown()


if __name__ == '__main__':
    asyncio.run(main())
