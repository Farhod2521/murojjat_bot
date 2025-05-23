from aiogram.utils.keyboard import InlineKeyboardBuilder

async def get_murojat_turlari(language: str = None):

    if language == "en":
        from data.en_malumotlar import murojat_turlari
        keyboard = InlineKeyboardBuilder()
        for key, value in murojat_turlari.items():
            keyboard.button(text=value, callback_data=key)
        
        return keyboard.adjust(2).as_markup()
    elif language == "ru":
        from data.ru_malumotlar import murojat_turlari
        keyboard = InlineKeyboardBuilder()
        for key, value in murojat_turlari.items():
            keyboard.button(text=value, callback_data=key)
        
        return keyboard.adjust(2).as_markup()
    else:
        from data.uz_malumotlar import murojat_turlari
        keyboard = InlineKeyboardBuilder()
        for key, value in murojat_turlari.items():
            keyboard.button(text=value, callback_data=key)
        
        return keyboard.adjust(2).as_markup()
    





# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


# step_two_buttons = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Shikoyat", callback_data="shikoyat"),
#             InlineKeyboardButton(text="Taklif", callback_data="taklif"),
#         ],
#         [
#             InlineKeyboardButton(text="Ariza", callback_data="ariza"),
#             InlineKeyboardButton(text="Boshqa", callback_data="boshqa"),
#         ],
#         [
#             InlineKeyboardButton(text="Orqaga", callback_data="orqaga"),
#         ],
#     ], 
# )
