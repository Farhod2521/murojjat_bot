

async def get_murojaat_text(language: str, data: dict, is_secondary: bool = False, to_user: bool = True):
    end_text = f"%{data.get('id')}%{data.get('lan')}%" if not to_user else ""
    
    if language == "en":
        title = "Application" if is_secondary else "New Application"
        return (
            f"🆕 <b>{title}</b>\n"
            f"<b>👤 User ID:</b> <code>{data.get('user_id') or data.get('user_tg_id')}</code>\n"
            f"<b>📌 User type:</b> {data.get('user_type') or data.get('your_position')}\n"
            f"<b>🎯 Purpose:</b> {data.get('murojaat_type')}\n"
            f"<b>📩 Addressed to:</b> {data.get('murojaat_to') or data.get('department')}\n"
            f"<b>🧑 Name:</b> {data['full_name']}\n"
            f"<b>📞 Phone:</b> <code>{data.get('phone_number') or data.get('phone')}</code>\n"
            f"<b>📝 Message:</b>\n<pre>{data.get('murojaat_text') or data.get('description')}</pre>\n"
            + end_text
        )

    elif language == "ru":
        title = "Oбращение" if is_secondary else "Новое обращение"
        return (
            f"🆕 <b>{title}</b>\n"
            f"<b>👤 ID пользователя:</b> <code>{data.get('user_id') or data.get('user_tg_id')}</code>\n"
            f"<b>📌 Тип пользователя:</b> {data.get('user_type') or data.get('your_position')}\n"
            f"<b>🎯 Цель обращения:</b> {data.get('murojaat_type')}\n"
            f"<b>📩 Кому:</b> {data.get('murojaat_to') or data.get('department')}\n"
            f"<b>🧑 Имя Фамилия:</b> {data['full_name']}\n"
            f"<b>📞 Телефон:</b> <code>{data.get('phone_number') or data.get('phone')}</code>\n"
            f"<b>📝 Текст обращения:</b>\n<pre>{data.get('murojaat_text') or data.get('description')}</pre>\n"
            + end_text
        )

    else:
        title = "Murojaat" if is_secondary else "🆕 <b>Yangi murojaat</b>"
        return (
            f"{title}\n"
            f"<b>👤 Foydalanuvchi ID:</b> <code>{data.get('user_id') or data.get('user_tg_id')}</code>\n"
            f"<b>📌 Foydalanuvchi turi:</b> {data.get('user_type') or data.get('your_position')}\n"
            f"<b>🎯 Murojaat maqsadi:</b> {data.get('murojaat_type')}\n"
            f"<b>📩 Murojaat kimga:</b> {data.get('murojaat_to') or data.get('department')}\n"
            f"<b>🧑 Ism Familiya:</b> {data['full_name']}\n"
            f"<b>📞 Telefon raqami:</b> <code>{data.get('phone_number') or data.get('phone')}</code>\n"
            f"<b>📝 Murojaat matni:</b>\n<pre>{data.get('murojaat_text') or data.get('description')}</pre>\n"
            + end_text
        )



async def get_murojaat_text_for_supper_admin(language: str, data: dict):
    if language == "en":
        return (
            f"🆕 <b>Application to {data.get('murojaat_to') or data.get('department')}</b>\n"
            f"👤 User ID: ({data.get('user_id') or data.get('user_tg_id')})\n"
            f"📌 User type: {data.get('user_type') or data.get('your_position')}\n"
            f"🎯 Application purpose: {data.get('murojaat_type')}\n"
            f"👤 Name Surname: {data.get('full_name')}\n"
            f"📞 Phone number: {data.get('phone_number') or data.get('phone')}\n"
            f"📝 Application text: {data.get('murojaat_text') or data.get('description')}\n"
            f"%{data.get('id')}%{data.get('lan')}%"
        )
    elif language == "ru":
        return (
            f"🆕 <b> Oбращение к {data.get('murojaat_to') or data.get('department')}</b>\n"
            f"👤 ID пользователя: ({data.get('user_id') or data.get('user_tg_id')}) \n"
            f"📌 Тип пользователя: {data.get('user_type') or data.get('your_position')}\n"
            f"🎯 Цель обращения: {data.get('murojaat_type')}\n"
            f"👤 Имя Фамилия: {data.get('full_name')}\n"
            f"📞 Номер телефона: {data.get('phone_number') or data.get('phone')}\n"
            f"📝 Текст обращения: {data.get('murojaat_text') or data.get('description')}\n"  
            f"%{data.get('id')}%{data.get('lan')}%"
        )
    else:
        return (
            f"🆕 <b>Murojaat {data.get('murojaat_to') or data.get('department')} ga kelib tushdi</b>\n"
            f"👤 Foydalanuvchi ID: ({data.get('user_id') or data.get('user_tg_id')})\n"
            f"📌 Foydalanuvchi turi: {data.get('user_type') or data.get('your_position')}\n"
            f"🎯 Murojaat maqsadi: {data.get('murojaat_type')}\n"
            f"👤 Ism Familiya: {data['full_name']}\n"
            f"📞 Telefon raqami: {data.get('phone_number') or data.get('phone')}\n"
            f"📝 Murojaat matni: {data.get('murojaat_text') or data.get('description')}\n"
            f"%{data.get('id')}%{data.get('lan')}%"
        )