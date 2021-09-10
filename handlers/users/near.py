from aiogram import types
from loader import dp
from my_types import User, Place
from states.near_location import Near
from aiogram.types import ContentType
from aiogram.dispatcher import FSMContext
from api.google_distance import get_nearest_locations, Location


@dp.message_handler(commands=["near"])
async def nearest_places(message: types.Message):
    await message.answer("Пришлите пожалуйста геолокацию.")
    await Near.location.set()


@dp.message_handler(state=Near.location, content_types=[ContentType.LOCATION, ContentType.VENUE])
async def get_place_location(message: types.Message, state: FSMContext):
    location = message.location
    longitude, latitude = location.longitude, location.latitude
    user = User(message.from_user.id)
    place = Place(-1, "test", longitude=longitude, latitude=latitude)
    nearest_locations = await get_nearest_locations(user, place)
    if len(nearest_locations) == 0:
        await message.answer(text="В радиусе 1.5 км избранных мест нет.")
    else:
        for loc in nearest_locations:
            await message.answer(text=f"{loc.place.name}")
            await message.answer_location(loc.place.latitude, loc.place.longitude)
    await state.finish()