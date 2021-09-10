from aiogram import types
from loader import dp
from utils.db_api.db_methods import delete_user_places


@dp.message_handler(commands=["reset"])
async def reset_places(message: types.Message):
    user_id = message.from_user.id
    delete_user_places(user_id)
    await message.answer(text="Все ваши места были успешно удалены.")
