from aiogram import types
from app.keyboards.inline.languages import languages_buttons
from aiogram.fsm.context import FSMContext

async def start_command(message: types.Message, state: FSMContext):

    await message.answer("Assalomu Alaykum!\n  Qulay tilni tanlang!", reply_markup=languages_buttons)