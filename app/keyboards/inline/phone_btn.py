from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def get_phone_btn(language: str = None) -> ReplyKeyboardMarkup:
    texts = {
        "en": "📞 Send phone number",
        "ru": "📞 Отправить номер телефона",
        "uz": "📞 Telefon raqamini yuborish"
    }

    # Agar til yo'q yoki topilmasa, default qilib 'uz' ni ishlatamiz
    text = texts.get(language, texts["uz"])

    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=text, request_contact=True)]],
        resize_keyboard=True
    )