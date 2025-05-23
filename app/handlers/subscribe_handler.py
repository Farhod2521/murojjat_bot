from aiogram import Router
from aiogram import types, F
from app.keyboards.inline.menu_btns import get_menu
from app.keyboards.inline.subscribe_btn import get_channels_keyboard
from app.utils import check_subscription, dict_keys_to_set
from data.uz_malumotlar import CHANNELS, path_to_channel
from app.keyboards.inline.languages import languages_buttons
from aiogram.fsm.context import FSMContext

subscription_router = Router()

@subscription_router.callback_query(F.data == "check_subscription")
async def subscribtion_han(callback: types.CallbackQuery, state: FSMContext):

    not_subscribed = await check_subscription(bot=callback.bot, user_id=callback.from_user.id, channels=CHANNELS)
    user_data = await state.get_data()
    language = user_data.get("language")

    if not_subscribed:
        not_sub_channels = {channel: CHANNELS[channel] for channel in not_subscribed}
        keyboard = await get_channels_keyboard(not_sub_channels, language=language)
        if language == "en":
            await callback.answer(
                "🚀 To use the bot, subscribe to the following channels:",
                reply_markup=keyboard
            )
        elif language == "ru":
            await callback.answer(
                "🚀 Чтобы использовать бота, подпишитесь на следующие каналы:",
                reply_markup=keyboard
            )
        else:
            await callback.answer(
                "🚀 Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling:",
                reply_markup=keyboard
            )
        return
        
    if language is None:
        await callback.message.edit_text(
                "Qulay tilni tanlang!", reply_markup=languages_buttons
            )
    else:
        if language == "en":
            await callback.message.edit_text(
                "Main menu", reply_markup=await get_menu(language)
            )
        elif language == "ru":
            await callback.message.edit_text(
                "Главное меню", reply_markup=await get_menu(language)
            )
        else:
            await callback.message.edit_text(
                "Asosiy menyu", reply_markup=await get_menu(language)
            )
            