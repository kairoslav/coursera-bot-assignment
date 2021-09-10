from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from my_types import User
from utils.db_api.db_methods import add_user


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user = User(message.from_user.id)
    add_user(user)
    await message.answer(f"Привет, {message.from_user.full_name}!")
