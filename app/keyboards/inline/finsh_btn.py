from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def get_finish_btn(language: str) -> InlineKeyboardMarkup:
    finish_buttons = None
    if language == "en":
        finish_buttons = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="✅ Send", callback_data="send"),
                ],
                [
                    InlineKeyboardButton(text="❌ Cancel", callback_data="cancel")
                ],
            ], 
        )
    elif language == "ru":
        finish_buttons = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="✅ Отправить", callback_data="send"),
                ],
                [
                    InlineKeyboardButton(text="❌ Отменить", callback_data="cancel")
                ],
            ], 
        )
    else:
        finish_buttons = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text="✅ Yuborish", callback_data="send"),
                ],
                [
                    InlineKeyboardButton(text="❌ Bekor qilish", callback_data="cancel")
                ],
            ], 
        )
    return finish_buttons

