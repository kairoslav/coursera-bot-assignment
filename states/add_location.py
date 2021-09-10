from aiogram.dispatcher.filters.state import StatesGroup, State


class Add(StatesGroup):
    text = State()
    photo = State()
    location = State()
