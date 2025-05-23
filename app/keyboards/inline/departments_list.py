from aiogram.utils.keyboard import InlineKeyboardBuilder
from data import uz_malumotlar, ru_malumotlar, en_malumotlar

async def get_xodimlar(language: str = None):

    if language == "en":
        from data.en_malumotlar import departments
        keyboard = InlineKeyboardBuilder()
        for key, value in departments.items():
            keyboard.button(text=value.name, callback_data=key)
        
        return keyboard.adjust(2,1,2,2,2,2,2,2,2,2).as_markup()
    elif language == "ru":
        from data.ru_malumotlar import departments
        keyboard = InlineKeyboardBuilder()
        for key, value in departments.items():
            keyboard.button(text=value.name, callback_data=key)
        
        return keyboard.adjust(2,1,2,2,2,2,2,2,2,2).as_markup()
    else:
        from data.uz_malumotlar import departments
        keyboard = InlineKeyboardBuilder()
        for key, value in departments.items():
            keyboard.button(text=value.name, callback_data=key)
        
        return keyboard.adjust(2,1,2,2,2,2,2,2,2,2).as_markup()
    

