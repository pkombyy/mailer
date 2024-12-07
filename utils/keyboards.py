from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Основная клавиатура для обычных пользователей
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Выслать сообщение')],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите, чтобы начать"
)

# Клавиатура для выбора действий после отправки сообщения
retry_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Отправить заново')],
        [KeyboardButton(text='Отправить новую ссылку')],
        [KeyboardButton(text='Отправить новое письмо')],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие"
)

# Административная клавиатура для администраторов
admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Добавить пользователя")],
        [KeyboardButton(text="Удалить пользователя")],
        [KeyboardButton(text="Просмотреть разрешенных пользователей")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Управление пользователями"
)

# Клавиатура для подтверждения действий
confirm_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Да')],
        [KeyboardButton(text='Нет')],
    ],
    resize_keyboard=True,
    input_field_placeholder="Подтвердите действие"
)

# Клавиатура для уведомления о статусе бота
status_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Проверить статус бота')],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие"
)

# Экспорт клавиатур
__all__ = [
    'main',
    'retry_keyboard',
    'admin_kb',
    'confirm_keyboard',
    'status_keyboard'
]