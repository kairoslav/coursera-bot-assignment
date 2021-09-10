from aiogram import types
from aiogram.dispatcher import FSMContext
from states.add_location import Add
from loader import dp


# обработка неправильно введенных данных на стадии приема названия места
from states.near_location import Near


@dp.message_handler(state=Add.text, content_types=types.ContentTypes.ANY)
async def text_is_not_correct(message: types.Message):
    await message.answer(f"К сожалению, я вас не понял.\n"
                         f"Введите название для места.")


# обработка неправильно введенных данных на стадии приема объекта геолокации места
@dp.message_handler(state=Add.location, content_types=types.ContentType.ANY)
async def location_is_not_correct(message: types.Message):
    await message.answer(f"У сожалению, я вас не понял.\n"
                         f"Отправьте геолокацию места.")


@dp.message_handler(state=Near.location, content_types=types.ContentType.ANY)
async def location_is_not_correct(message: types.Message):
    await message.answer(f"У сожалению, я вас не понял.\n"
                         f"Отправьте геолокацию места.")


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Я вас не понял.\n"
                         f"Список доступных комманд - /help")


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    # state = await state.get_state()
    await message.answer(f"Я вас не понял.\n"
                         f"Список доступных комманд - /help")
