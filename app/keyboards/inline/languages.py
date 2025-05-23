from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


languages_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇺🇿 O'zbek", callback_data="uz"),
        ],
        [
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru")
        ],
        [
            InlineKeyboardButton(text="🏴󠁧󠁢󠁥󠁮󠁧󠁿 English", callback_data="en"),
        ],
   
    ], 
)
