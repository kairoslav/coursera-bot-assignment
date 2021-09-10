from aiogram.dispatcher.filters.state import StatesGroup, State


class Near(StatesGroup):
    location = State()
