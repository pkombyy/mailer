from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.state import AddUser, RemoveUser
from config import ALLOWED_USERS
from utils.functions import is_admin, get_user_id_by_username
router = Router()

@router.message(F.text == "Добавить пользователя")
async def start_add_user(message: Message, state: FSMContext):
    if not is_admin(message.from_user.id):
        await message.answer("У вас нет прав для добавления пользователей.")
        return
    await message.answer("Введите @username или список через запятую/пробелы.")
    await state.set_state(AddUser.username)

@router.message(AddUser.username)
async def add_allowed_users(message: Message, state: FSMContext):
    usernames = message.text.replace(",", " ").split()
    added_users = []
    failed_users = []

    for username in usernames:
        user_id = await get_user_id_by_username(username)
        if user_id and user_id not in ALLOWED_USERS:
            ALLOWED_USERS.add(user_id)
            added_users.append(username)
        else:
            failed_users.append(username)

    await message.answer(f"Добавлены: {', '.join(added_users)}\nНе добавлены: {', '.join(failed_users)}")
    await state.clear()

@router.message(F.text == "Удалить пользователя")
async def start_remove_user(message: Message, state: FSMContext):
    if not is_admin(message.from_user.id):
        await message.answer("У вас нет прав для удаления пользователей.")
        return
    await message.answer("Введите @username или список через запятую/пробелы для удаления.")
    await state.set_state(RemoveUser.username)

@router.message(RemoveUser.username)
async def remove_allowed_users(message: Message, state: FSMContext):
    usernames = message.text.replace(",", " ").split()
    removed_users = []
    failed_users = []

    for username in usernames:
        user_id = await get_user_id_by_username(username)
        if user_id and user_id in ALLOWED_USERS:
            ALLOWED_USERS.remove(user_id)
            removed_users.append(username)
        else:
            failed_users.append(username)

    await message.answer(f"Удалены: {', '.join(removed_users)}\nНе удалены: {', '.join(failed_users)}")
    await state.clear()
