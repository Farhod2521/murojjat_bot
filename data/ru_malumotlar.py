# from app.states import Xodim
# from data import employees_and_departments

# ###################################################
# ######## 👇 Universitet xodimlari uchun 👇 #########
# ###################################################

# rektor = Xodim('Ректор', list_of_tg_id=[employees_and_departments.arslon, employees_and_departments.feruz, employees_and_departments.nuriddin])
# korupsiya = Xodim('Борьба против коррупции', 917999618)
# qabul = Xodim('Приемная комиссия', 917999618)
# buxgalteriya = Xodim('Бухгалтерский учет', 917999618)
# registrator = Xodim('Офис регистратора', 917999618)
# hemis = Xodim('Хемис', 85942449)


# # 👇 Xodim kiritilgandan So'ng Pastga ham qo'shiladi 👇

# xodimlar = {
#     'rektor': rektor,
#     'hemis': hemis,
#     'korupsiya': korupsiya,
#     'buxgalteriya': buxgalteriya,
#     'registrator': registrator,
#     'qabul': qabul,
# }


from app.states import Employee, Department

# Xodimlar ro'yxatini yaratish
farhod = Employee(name='Farhod',  tg_id=1858379541)


# departamentlar ro'yxatini yaratish
rektorat = Department(name='Rahbariyat', list_of_employees=[farhod])
kr = Department(name='Korupsiyaga qarshi', list_of_employees=[farhod])
bugalteriya = Department(name='Buxgalteriya', list_of_employees=[farhod])
tm = Department(name="Texnik me'yorlash", list_of_employees=[farhod])
st = Department(name='Standartlashtirish', list_of_employees=[farhod])
xa = Department(name='Xalaqaro aloqalar', list_of_employees=[farhod])

ab = Department(name="AKT bo'lim", list_of_employees=[farhod])
l = Department(name='Laboratoriya', list_of_employees=[farhod])
kl= Department(name='Klassifikator', list_of_employees=[farhod])


departments = {
    'rahbariyat': rektorat,
    'kr': kr,
    'bugalteriya': bugalteriya,
    'tm': tm,
    'st': st,
    'xa': xa,
    'ab': ab,
    'l': l,
    'kl': kl,
}



###################################################
######## Murojat qilivchilar uchun ################
###################################################

murojatchilar = {
    'fuqpro': '🙍🏻‍♂️ Гражданин',  
    'xodim': '👨‍💻 Сотрудник',  
    'boshqa': '🔄 Другой',  
    'orqaga': '⬅️ Назад',  
}


###################################################
################ Murojaat turi. ###################
###################################################


murojat_turlari = {
    'shikoyat': 'Жалоба',
    'taklif': 'Предложение',
    'ariza': 'Заявка',
    'boshqa': 'Другой',
    'orqaga': '⬅️ Назад',
}


###################################################
################# CHANNELS ########################
###################################################
path_to_channel ='https://t.me/'
CHANNELS = {
    "@tmsiti": "TMSITI|Официальный канал",
}

SUPER_ADMIN = 1858379541
""" Super admin, Javob yuborilganligini ko'rish """