import re
from data.uz_malumotlar import CHANNELS,  SUPER_ADMIN
from aiogram.exceptions import TelegramBadRequest
from typing import Tuple
import logging
from data import uz_malumotlar, ru_malumotlar, en_malumotlar

UZ_PHONE_REGEX = r"^(?:\+998|998)?(90|91|93|94|95|97|98|99|33|88)\d{7}$"
pattern = r"^\+998\d{9}$|^\d{9}$"


def get_package_by_lang(lang: str):

    if lang == "ru":
        return ru_malumotlar
    elif lang == "en":
        return en_malumotlar
    else:
        return uz_malumotlar


def dict_keys_to_set(dictionary):
    return set(dictionary.keys())



    




# def get_user_tg_id(name: str, lang: str) -> set[int]:
#     employees = get_package_by_lang(lang=lang).xodimlar
#     list_of_tg_id = set()

#     for key, employee in employees.items():
#         if employee.name == name:
#             if employee.tg_id is not None:
#                 list_of_tg_id.add(employee.tg_id)
            
#             if employee.list_of_tg_id:
#                 for xodim in employee.list_of_tg_id:
#                     if xodim.tg_id is not None:
#                         list_of_tg_id.add(xodim.tg_id)

#     return list_of_tg_id




# def get_admin_users_id(user_id):
#     for key in xodimlar:
#         xodim = xodimlar[key]
#         if xodim.tg_id == user_id:
#             return True
        
#         if xodim.list_of_tg_id:
#             for sub_xodim in xodim.list_of_tg_id:
#                 if sub_xodim.tg_id == user_id:
#                     return True

#     if user_id == SUPER_ADMIN:
#         return True
    
#     return False 

# def get_admins_id_by_department(department: str, lang: str) -> set[int]:
#     employees = get_package_by_lang(lang=lang).xodimlar
#     list_of_tg_id = set()

#     for key, employee in employees.items():
#         if employee.name == department:
#             if employee.tg_id is not None:
#                 list_of_tg_id.add(employee.tg_id)
            
#             if employee.list_of_tg_id:
#                 for xodim in employee.list_of_tg_id:
#                     if xodim.tg_id is not None:
#                         list_of_tg_id.add(xodim.tg_id)

#     return list_of_tg_id




# def get_admin_name(admin_id, lang: str, employee: str= None):
#     employees = get_package_by_lang(lang=lang).xodimlar
#     for key, xodim in employees.items():
#         if xodim.tg_id == admin_id:
#             return xodim.name

#         if xodim.list_of_tg_id:
#             for sub_xodim in xodim.list_of_tg_id:
#                 if sub_xodim.tg_id == admin_id:
#                     return sub_xodim.name

#     return "Mutaxassis"







def extract_number_and_text(text):
    match = re.search(r'%(\d+)%([a-zA-Z]{2})%\s*$', text)
    if match:
        number = match.group(1)  
        text = match.group(2) 
        return number, text
    return None, None


def extract_text(text):
    start = text.find("(")
    end = text.find(")", start)
    if start != -1 and end != -1:
        return text[start+1:end]  # Qavslarni o‘chirib, faqat ichidagi matnni olish
    return None

def phone_reg(number):
    if re.match(pattern, number):
        return True
    return False


def format_phone_number(phone: str) -> str:
    # Faqat raqamlarni olish
    digits = re.sub(r"\D", "", phone)

    # Telefon raqami uzunligini tekshiramiz
    if len(digits) == 9:  # 9 xonali raqam
        return f"+998 {digits[:2]} {digits[2:5]} {digits[5:7]} {digits[7:9]}"
    elif len(digits) == 12 and digits.startswith("998"):  # To‘liq +998 bilan kelgan raqam
        return f"+{digits[:3]} {digits[3:5]} {digits[5:8]} {digits[8:10]} {digits[10:12]}"
    else:
        return "❌ Noto‘g‘ri raqam"


async def is_not_subscribed(bot, user_id: int, channel: str) -> bool:
    """Foydalanuvchi obuna bo‘lmagan kanalni tekshiradi."""
    try:
        member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
        return member.status in {"left", "kicked"}
    except TelegramBadRequest as e:
        logging.error(f"Kanalni tekshirishda xatolik: {e}")
        return True  
    

async def check_subscription(bot, user_id: int, channels: set[str]):
    """Foydalanuvchining barcha kanallarga obuna bo'lganligini tekshiradi."""
    not_subscribed = [
        channel
        for channel in channels
        if await is_not_subscribed(bot, user_id, channel)
    ]
    return not_subscribed


def beauty_print(data: dict):
    for key in data:
        print(f"key: {data[key]}\n")

