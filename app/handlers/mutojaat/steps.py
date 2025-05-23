from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
import re
from data.texts.text_of_murojaat import get_murojaat_text, get_murojaat_text_for_supper_admin
from app.keyboards.inline.applicants_type_buttons import get_murojatchilar     #step_one_buttons
from app.keyboards.inline.applications_type_buttons import get_murojat_turlari   #step_two_buttons
from app.keyboards.inline.departments_list import get_xodimlar        # step_three_buttons
from app.keyboards.inline.phone_btn import get_phone_btn
from app.keyboards.inline.finsh_btn import  get_finish_btn
from app.states import MurojaatStates
from app.utils import dict_keys_to_set, phone_reg, format_phone_number, get_package_by_lang
from app.keyboards.inline.menu_btns import get_menu
from data.uz_malumotlar import departments, murojatchilar, murojat_turlari, SUPER_ADMIN
from app.new_functions import get_employees_by_department # Xodimlarni name va tg_id bilan olish


murojaat_router = Router()


"""Murojaat tugmasi bosilganda"""
@murojaat_router.callback_query(F.data == "murojaat")
async def step_one(callback: types.CallbackQuery, state: FSMContext):
    
    await state.update_data(user_tg_id=callback.from_user.id)
    
    data = await state.get_data()
    language = data.get('language')
    answer_text = None
    
    if language == "ru":
        answer_text = "Кто обращается?"
    elif language == "en": 
        answer_text = "Who is applying?"
    else:
        answer_text = "Kim murojaat qilmoqda?"

    await state.set_state(MurojaatStates.step_one)
    await callback.message.edit_text(
        text=answer_text, reply_markup=await get_murojatchilar(language=language)
    )


"""Murojaat qiluvchi kimligini tanlash tugmasi bosilganda"""
@murojaat_router.callback_query(F.data.in_(dict_keys_to_set(murojatchilar)), MurojaatStates.step_one)
async def step_two(callback: types.CallbackQuery, state: FSMContext):

    user_dates = await state.get_data()
    language = user_dates.get('language')
    
    answer_text = ""

    await state.update_data(user_type=get_package_by_lang(lang=language).murojatchilar.get(callback.data))
    await state.set_state(MurojaatStates.step_two)
    if callback.data == 'orqaga':
        back_text = ""
        if language == "ru":
            back_text = "Главное меню"
        elif language == "en": 
            back_text = "Main menu"
        else:
            back_text = "Asosiy menyu"

        await state.set_state(MurojaatStates.step_one)
        await callback.message.edit_text(
            text=back_text, reply_markup=await get_menu(language=language)
        )
        return
    
    else:
        if language == "ru":
            answer_text = "Цель апелляции?"
        elif language == "en": 
            answer_text = "Purpose of the appeal?"
        else:
            answer_text = "Murojaat maqsadi?"

        await callback.message.edit_text(
            text=answer_text, reply_markup=await get_murojat_turlari(language=user_dates.get('language'))
        )

"""Murojaat maqsadi tugmasi bosilganda"""
@murojaat_router.callback_query(F.data.in_(dict_keys_to_set(murojat_turlari)), MurojaatStates.step_two)
async def step_three(callback: types.CallbackQuery, state: FSMContext):
    user_dates = await state.get_data()
    language = user_dates.get('language')
    
    if callback.data == 'orqaga':
        back_text = ""
        if language == "ru":
            back_text = "Кто обращается?"
        elif language == "en": 
            back_text = "Who is applying?"
        else:
            back_text = "Kim murojaat qilmoqda?"
        await state.set_state(MurojaatStates.step_one)
        await callback.message.edit_text(
            text=back_text, reply_markup=await get_murojatchilar(language=language)
        )
    else:
        answer_text = ""
        if language == "ru":
            answer_text = "Кому следует направлять заявку?"
        elif language == "en": 
            answer_text = "To whom should the application be sent?"
        else:
            answer_text = "Murojaat kimga yuborilishi kerak?"

        await state.update_data(murojaat_type=get_package_by_lang(lang=language).murojat_turlari.get(callback.data))
        await state.set_state(MurojaatStates.step_three)
        await callback.message.edit_text(
            text=answer_text, reply_markup=await get_xodimlar(language=user_dates.get("language"))
        )


"""Murojaat kimga yuborilishi kerak tugmasi bosilganda"""
@murojaat_router.callback_query(F.data.in_(dict_keys_to_set(departments)), MurojaatStates.step_three)
async def step_four(callback: types.CallbackQuery, state: FSMContext):
    user_dates = await state.get_data()
    language = user_dates.get('language')

    if callback.data == 'orqaga':
        back_text = ""
        if language == "ru":
            back_text = "📌 Кому следует направлять заявку?"
        elif language == "en": 
            back_text = "📌 To whom should the application be sent?"
        else:
            back_text = "📌 Murojaat kimga yuborilishi kerak?"
        
        await state.set_state(MurojaatStates.step_two)
        await callback.message.edit_text(
            text=back_text, reply_markup=await get_murojat_turlari(language=language)
        )
    else:
        await state.update_data(murojaat_to=get_package_by_lang(lang=language).departments.get(callback.data).name)
        await state.set_state(MurojaatStates.step_four)
        if language == "ru":
            await callback.message.edit_text(
                "👤 Введите ваше имя и фамилию:", reply_markup=None
            )
        elif language == "en":
            await callback.message.edit_text(
                "👤 Enter your name and surname:", reply_markup=None
            )
        else:
            await callback.message.edit_text(
                "👤 Ism Familiyangizni kiriting:", reply_markup=None
            )
        

"""Ism Familiya kiritilganda"""
@murojaat_router.message(MurojaatStates.step_four)
async def step_five(message: types.Message, state: FSMContext):
    user_dates = await state.get_data()
    language = user_dates.get('language')

    if 6 < len(message.text) < 30:
        await state.update_data(full_name=str(message.text))
        await state.set_state(MurojaatStates.step_five)
        
        if language == "ru":
            await message.answer(
                "📞 Введите номер телефона:", reply_markup=await get_phone_btn(language=language)
            )
        elif language == "en":
            await message.answer(
                "📞 Enter your phone number:", reply_markup=await get_phone_btn(language=language)
            )
        else:
            await message.answer(
                "📞 Telefon raqamingizni kiriting:", reply_markup=await get_phone_btn(language=language)
            )
    else:
        if language == "ru":
            await message.answer(
                "👤 Введите правильное имя!", reply_markup=types.ReplyKeyboardRemove()
            )
        elif language == "en":
            await message.answer(
                "👤 Enter your name correctly!", reply_markup=types.ReplyKeyboardRemove()
            )
        else:
            await message.answer(
                "👤 Ism Familiyangizni to'g'ri kiriting!", reply_markup=types.ReplyKeyboardRemove()
            )



"""Telefon raqami kiritilganda"""
@murojaat_router.message(MurojaatStates.step_five)
async def step_six(message: types.Message, state: FSMContext):
    phone_number = 0
    user_dates = await state.get_data()
    language = user_dates.get('language')
    if message.text:
        phone_number = message.text
    else:
        if len(message.contact.phone_number) == 12:
            phone_number = f"+{message.contact.phone_number}"
        else:
            phone_number = message.contact.phone_number

    if phone_reg(phone_number.replace(" ", "")):
        await state.update_data(phone_number=format_phone_number(phone_number))
        await state.set_state(MurojaatStates.step_six)
        if language == "ru":
            await message.answer(
                "📝 Введите текст обращения:", reply_markup=types.ReplyKeyboardRemove()
            )
        elif language == "en":
            await message.answer(
                "📝 Enter the text of the appeal:", reply_markup=types.ReplyKeyboardRemove()
            )
        else:
            # O'zbek tilida
            await message.answer(
                "📝 Murojaat matnini kiriting:", reply_markup=types.ReplyKeyboardRemove()
            )
    else:
        if language == "ru":
            await message.answer("Введите номер телефона \n+998 94 503 18 17 или 94 503 18 17 \nв формате номера!")
        elif language == "en":
            await message.answer("Enter the phone number \n+998 94 503 18 17 or 94 503 18 17 \nin the format of the number!")
        else:
            # O'zbek tilida
            await message.answer("Telefon raqamini \n+998 94 503 18 17 yoki 94 503 18 17 \nko'rinishida raqamni kiriting!")


"""Murojaat matni kiritilganda"""
@murojaat_router.message(MurojaatStates.step_six)
async def step_seven(message: types.Message, state: FSMContext):
    
    await state.update_data(murojaat_text=message.text)
    await state.set_state(MurojaatStates.step_seven)
    data = await state.get_data()
    language = data.get('language')
    if language == "ru":
        await message.answer(
            text= await get_murojaat_text(language=language, data=data), 
            parse_mode="HTML", reply_markup=await get_finish_btn(language=language)
        )
    elif language == "en":
        await message.answer(
            text= await get_murojaat_text(language=language, data=data), 
            parse_mode="HTML", reply_markup=await get_finish_btn(language=language)
        )
    else:
        # O'zbek tilida
        await message.answer(
            text= await get_murojaat_text(language=language, data=data), 
            parse_mode="HTML", reply_markup=await get_finish_btn(language=language)
        )


"""Murojaat yuborilganda"""
@murojaat_router.callback_query(F.data.in_({"send", "cancel"}), MurojaatStates.step_seven)
async def step_eight(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)  # Inline tugmalarni o‘chirish
    data = await state.get_data()
    language = data.get('language')
    if callback.data == 'send':
        # murojaat_id = await add_murojaat(
        #             user_tg_id=data.get('user_tg_id'),
        #             full_name=data.get('full_name'), 
        #             phone=data.get('phone_number'), 
        #             your_position=data.get('user_type'), 
        #             department=data.get('murojaat_to'),
        #             murojaat_type=data.get('murojaat_type'), 
        #             description=data.get('murojaat_text'))
        
        full_data = {
            "user_id": data.get('user_id'),
            "user_tg_id": data.get('user_tg_id'),
            "full_name": data.get('full_name'),
            "phone_number": data.get('phone_number'),
            "your_position": data.get('user_type'),
            "murojaat_type": data.get('murojaat_type'),
            "murojaat_to": data.get('murojaat_to'),
            "murojaat_text": data.get('murojaat_text'),
            "lan": language
        }

        department = data.get('murojaat_to')
        list_of_employees = get_employees_by_department(department=department, lang=language)

        for employee in list_of_employees:
            try:
                await callback.bot.send_message(chat_id=employee.tg_id, text=await get_murojaat_text(language=language, data=full_data, to_user=False), parse_mode="HTML")
            except Exception as e:
                print(f"⁉️ {employee.name} {employee.tg_id} : {e}")
                continue
        
        try:
            await callback.bot.send_message(chat_id=SUPER_ADMIN, text=await get_murojaat_text_for_supper_admin(language=language, data=full_data), parse_mode="HTML")
        except Exception as e:
            print(f"Error sending message to SUPER_ADMIN: {e}")
            pass
        
        await state.clear()
        
        if language:
            await state.update_data(language=language)

        if language == "ru":
            await callback.message.answer("✅ Ваша заявка отправлена.")
            await callback.message.answer("Ваша заявка будет рассмотрена в кратчайшие сроки.")
            await callback.message.answer("Главное меню", reply_markup=await get_menu(language=language))
        elif language == "en":
            await callback.message.answer("✅ Your application has been sent.")
            await callback.message.answer("Your request will be processed as soon as possible.")
            await callback.message.answer("Main menu", reply_markup=await get_menu(language=language))
        else:
            await callback.message.answer("✅ Murojaatingiz yuborildi.")
            await callback.message.answer("Murojaatingiz eng qisqa vaqt ichida ko'rib chiqiladi.")
            await callback.message.answer("Asosiy menu", reply_markup=await get_menu(language=language))
        
    else:
        await state.clear()
        if language:
            await state.update_data(language=language)
        
        if language == "ru":
            await callback.message.answer("❌ Ваша заявка отменена.")
            await callback.message.answer("Главное меню", reply_markup=await get_menu(language=language))
        elif language == "en":
            await callback.message.answer("❌ Your application has been canceled.")
            await callback.message.answer("Main menu", reply_markup=await get_menu(language=language))
        else:
            await callback.message.answer("❌ Murojaat bekor qilindi.")
            await callback.message.answer("Asosiy menu", reply_markup=await get_menu(language=language))
    
