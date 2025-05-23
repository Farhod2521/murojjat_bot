from aiogram.utils.keyboard import InlineKeyboardBuilder

# menu_btns = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Murojaat yo'llash", callback_data="murojaat"),
#         ],
#         [
#             InlineKeyboardButton(text="Mening murojaatlarim", callback_data="murojaatlarim"),
#         ],
#     ]
# )

async def get_menu(language: str = None):
    if language == "en":
        menu_items = {
            "murojaat": "📝 Submit an application",
            "murojaatlarim": "🗒 My appeals"
        }
        
        keyboard = InlineKeyboardBuilder()
        for key, value in menu_items.items():
            keyboard.button(text=value, callback_data=key)
        
        return keyboard.adjust(1).as_markup()
    elif language == "ru":
        menu_items = {
            "murojaat": "📝 Подать заявку",
            "murojaatlarim": "🗒 Мои апелляции"
        }
        
        keyboard = InlineKeyboardBuilder()
        for key, value in menu_items.items():
            keyboard.button(text=value, callback_data=key)
        
        return keyboard.adjust(1).as_markup()
    else:
        menu_items = {
            "murojaat": "📝 Murojaat yo'llash",
            "murojaatlarim": "🗒 Mening murojaatlarim"
        }
        
        keyboard = InlineKeyboardBuilder()
        for key, value in menu_items.items():
            keyboard.button(text=value, callback_data=key)
        
        return keyboard.adjust(1).as_markup()