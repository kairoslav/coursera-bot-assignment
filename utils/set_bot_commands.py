from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("add", "Добавление нового места"),
            types.BotCommand("near", "Места в радиусе 1.5 км"),
            types.BotCommand("list", "Показать добавленные места"),
            types.BotCommand("reset", "Удалить все места"),
            types.BotCommand("help", "Показать справку")
        ]
    )
