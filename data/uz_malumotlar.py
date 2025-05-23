# from app.states import Xodim
# from data import employees_and_departments
# ###################################################
# ######## 👇 Universitet xodimlari uchun 👇 #########
# ###################################################

# rektor = Xodim(name='Rektor', list_of_tg_id=[employees_and_departments.feruz, employees_and_departments.nuriddin, employees_and_departments.arslon])
# korupsiya = Xodim('Korupsiyaga qarshi kurashish', 917999618)
# qabul = Xodim('Qabul komisyasi', 917999618)
# buxgalteriya = Xodim('Buxgalteriya', 917999618)
# registrator = Xodim('Registrator ofis', 917999618)
# hemis = Xodim('Hemis', 85942449)


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
    'fuqpro': '🙍🏻‍♂️ Fuqaro',
    'xodim': '👨‍💻 Xodim',

    'boshqa': '🔄 Boshqa',
    'orqaga': '⬅️ Orqaga',
}

###################################################
################ Murojaat turi. ###################
###################################################

murojat_turlari = {
    'shikoyat': 'Shikoyat',
    'taklif': 'Taklif',
    'ariza': 'Ariza',
    'boshqa': 'Boshqa',
    'orqaga': '⬅️ Orqaga',
}

###################################################
################# CHANNELS ########################
###################################################
path_to_channel ='https://t.me/'

CHANNELS = {
    "@tmsiti": "TMSITI|Rasmiy kanali",
}


""" Super admin, Javob yuborilganligini ko'rish """

SUPER_ADMIN = 1858379541