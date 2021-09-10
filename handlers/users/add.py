from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
from loader import dp
from states.add_location import Add
from my_types import Place, User
from utils.db_api.db_methods import get_last_place_id, add_place_for_user


@dp.message_handler(commands=["add"])
async def add(message: types.Message):
    await message.answer("Пришлите название места, которое хотите добавить.")
    await Add.text.set()


@dp.message_handler(state=Add.text)
async def get_place_name(message: types.Message, state: FSMContext):
    place_name = message.text
    await state.update_data(name=place_name)
    await message.answer("Теперь пришлите его геолокацию.")
    await Add.location.set()


@dp.message_handler(state=Add.location, content_types=[ContentType.LOCATION, ContentType.VENUE])
async def get_place_location(message: types.Message, state: FSMContext):
    location = message.location
    longitude, latitude = location.longitude, location.latitude
    data = await state.get_data()
    place_name = data.get('name')
    place_id = get_last_place_id()
    place = Place(
        place_id+1,
        place_name,
        longitude,
        latitude
    )
    user = User(message.from_user.id)
    add_place_for_user(user, place)
    await state.finish()
    await message.answer(text="Место было успешно добавлено!")

