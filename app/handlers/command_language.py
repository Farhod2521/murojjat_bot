from aiogram import types
from aiogram.filters import Command
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from app.keyboards.inline.languages import languages_buttons


async def language_command(message: types.Message, state: FSMContext):
    await message.answer("Qulay tilni tanlang!", reply_markup=languages_buttons)



