
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram import BaseMiddleware
from app.keyboards.inline.menu_btns import get_menu

router = Router()

@router.callback_query(F.data.in_(['uz', 'ru', 'en']))
async def language_callback(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(language=callback.data)
    if callback.data == "en":
        await callback.answer("Language changed successfully!")
        await callback.message.edit_text(
            "Main menu!", reply_markup=await get_menu(language=callback.data)
        )
    elif callback.data == "ru":
        await callback.answer("Язык успешно изменен!")
        await callback.message.edit_text(
            "Главное меню!", reply_markup=await get_menu(language=callback.data)
        )
    else:
        await callback.answer("Til muvaffaqiyatli o'zgartirildi!")
        await callback.message.edit_text(
            "Asosiy menu!", reply_markup=await get_menu(language=callback.data)
        )
