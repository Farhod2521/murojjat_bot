from aiogram.filters import CommandStart, Command
from aiogram import Bot, Dispatcher
import logging
import asyncio

from app.handlers.start import start_command
from app.handlers import language_handler
from app.handlers.command_language import language_command
from app.handlers.mutojaat.steps import murojaat_router
from app.handlers.admin.handlers import admin_router
from app.handlers.help import help_command
from aiogram.types import BotCommand

bot = Bot(token="6698622878:AAGeZkrsBOzlIxiB8D-5iKbyyQViUYYnYt8")
dp = Dispatcher()

async def main():
    dp.message.register(start_command, CommandStart())
    dp.message.register(help_command, Command(commands=["help"]))
    dp.message.register(language_command, Command(commands=["language"]))
    await bot.set_my_commands([
        BotCommand(command="/start", description="Bosh sahifa"),
        BotCommand(command="/help", description="Yordam"),
        BotCommand(command="/language", description="Tilni tanlash"),
    ])

    dp.include_router(language_handler.router)
    dp.include_router(murojaat_router)
    dp.include_router(admin_router)


    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__": 
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped.")


