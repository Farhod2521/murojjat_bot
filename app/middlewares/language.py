from typing import Callable, Awaitable, Dict, Any
from aiogram.types import TelegramObject
from aiogram import BaseMiddleware
from aiogram.types import Message
from app.keyboards.inline.languages import languages_buttons
from aiogram.fsm.context import FSMContext

class LanguageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        if isinstance(event, Message):
            print("State :")
            state: FSMContext = data.get("state")
    
            if state:
                user_data = await state.get_data()
                if "language" not in user_data:
                    await event.answer("Iltimos, tilni tanlang:", reply_markup=languages_buttons)
                    return
        return await handler(event, data)
