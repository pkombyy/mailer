from aiogram.fsm.state import State, StatesGroup

class OnWork(StatesGroup):
    email = State()  # Состояние для ввода email
    url = State()    # Состояние для ввода ссылки

class RemoveUser (StatesGroup):
    username = State()  # Состояние для удаления пользователя

class AddUser (StatesGroup):
    username = State()  # Состояние для добавления пользователя

class ConfirmAction(StatesGroup):
    confirm = State()  # Состояние для подтверждения действия