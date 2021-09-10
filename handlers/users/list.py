from aiogram import types
from loader import dp
from my_types import Place
from utils.db_api.db_methods import get_user_places


@dp.message_handler(commands=["list"])
async def get_list(message: types.Message):
    user_places = get_user_places(message.from_user.id)
    for user_place in user_places[-10:]:
        place = Place(*user_place[:4])
        await message.answer(text=f"{place.name}")
        await message.answer_location(place.latitude, place.longitude)
    if len(user_places) == 0:
        await message.answer(text="Список мест пуст.")
