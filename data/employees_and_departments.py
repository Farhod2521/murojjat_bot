from app.states import Employee, Department

# Xodimlar ro'yxatini yaratish
feruz = Employee(name='Feruzbek',  tg_id=1858379541)
nuriddin = Employee(name='Nuriddin', tg_id=1858379541)
arslon = Employee(name='Arslonbek', tg_id=1858379541)


# departamentlar ro'yxatini yaratish
rektorat = Department(name='Rektorat', list_of_employees=[feruz, nuriddin, arslon])
hemis = Department(name='Hemis', list_of_employees=[feruz, nuriddin, arslon])
bugalteriya = Department(name='Bugalteriya', list_of_employees=[feruz, nuriddin, arslon])

departments = {
    'rektorat': rektorat,
    'hemis': hemis,
    'bugalteriya': bugalteriya,
}
