from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from utils.keyboards import main_keyboard
from config import ALLOWED_USERS, ADMIN_IDS
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id  # Получаем ID пользователя
    logging.info(f"Получен ID пользователя: {user_id}")  # Логируем ID пользователя

    if not (user_id in ALLOWED_USERS) and not (user_id in ADMIN_IDS):
        await message.answer("У вас нет доступа к этому боту.")
        return
    
    await message.answer(">>>Бот запущен<<<", reply_markup=main_keyboard)
