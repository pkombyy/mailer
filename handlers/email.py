from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.state import OnWork
from validators import email, url
from utils.functions import send_email

router = Router()

@router.message(F.text == 'Выслать сообщение')
async def request_email(message: Message, state: FSMContext):
    await message.answer("Введите email получателя:")
    await state.set_state(OnWork.email)

@router.message(OnWork.email)
async def validate_email(message: Message, state: FSMContext):
    if not email(message.text):
        await message.answer("Некорректный email. Пожалуйста, введите корректный email:")
        return
    await state.update_data(email=message.text)
    await message.answer("Введите ссылку для отправки:")
    await state.set_state(OnWork.url)

@router.message(OnWork.url)
async def validate_url(message: Message, state: FSMContext):
    if not url(message.text):
        await message.answer("Некорректная ссылка. Пожалуйста, введите корректную ссылку:")
        return
    user_data = await state.get_data()
    email_address = user_data.get("email")
    link = message.text
    
    if await send_email(email_address, link):
        await message.answer("Письмо успешно отправлено!")
    else:
        await message.answer("Ошибка при отправке письма. Попробуйте еще раз.")
    await state.clear()
