from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/add - Добавление нового места",
            "/near - Места в радиусе 1.5 км",
            "/list - Показать добавленные места",
            "/reset - Удалить все места",
            "/help - Получить справку")
    
    await message.answer("\n".join(text))
