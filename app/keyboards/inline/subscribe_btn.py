from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from data.uz_malumotlar import CHANNELS, path_to_channel


from aiogram.utils.keyboard import InlineKeyboardBuilder

async def get_channels_keyboard(channels:dict, language: str = None):
    if language == "en":
        keyboard = InlineKeyboardBuilder()
        for key, value in channels.items():
            channel_link = f"{path_to_channel}{key.lstrip('@')}"
            keyboard.button(text=value, url=channel_link)

        keyboard.button(text="✅ Obuna bo'ldim", callback_data="check_subscription")
        
        return keyboard.adjust(1).as_markup()
    elif language == "ru":
        keyboard = InlineKeyboardBuilder()
        for key, value in channels.items():
            channel_link = f"{path_to_channel}{key.lstrip('@')}"
            keyboard.button(text=value, url=channel_link)

        keyboard.button(text="✅ Подписался", callback_data="check_subscription")
        
        return keyboard.adjust(1).as_markup()
    else:
        keyboard = InlineKeyboardBuilder()
        for key, value in channels.items():
            channel_link = f"{path_to_channel}{key.lstrip('@')}"
            keyboard.button(text=value, url=channel_link)

        keyboard.button(text="✅ Obuna bo'ldim", callback_data="check_subscription")
        
        return keyboard.adjust(1).as_markup()
