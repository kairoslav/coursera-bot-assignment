from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from my_types import User
from utils.db_api.db_methods import add_user


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = User(message.from_user.id)
    add_user(user)
    commands = (
        f"Привет, {message.from_user.full_name}!\n",
        "Доступные команды:",
        "/add - Добавление нового места",
        "/near - Места в радиусе 1.5 км",
        "/list - Показать добавленные места",
        "/reset - Удалить все места",
        "/help - Получить справку"
    )
    await message.answer(text="\n".join(commands))

