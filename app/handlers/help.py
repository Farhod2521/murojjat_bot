from aiogram import types
from aiogram.filters import Command


async def help_command(message: types.Message):
    await message.answer("This is the help section. How can I assist you today?")

