from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="Да"), KeyboardButton(text="Нет")]
    ]
)
