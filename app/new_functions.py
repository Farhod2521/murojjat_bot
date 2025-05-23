
# from data.employees_and_departments import departments
from app.utils import get_package_by_lang
from data.uz_malumotlar import SUPER_ADMIN, departments
from app.states import Employee



# murojaatni xodimlarga yuborish uchun
def get_employees_by_department(department: str, lang: str) -> list[Employee]:
    department_dict = get_package_by_lang(lang=lang).departments

    for key, dep  in department_dict.items():
        if dep.name == department:
            return list(dep.list_of_employees)
        
    return list([Employee(name="Super Admin", tg_id=SUPER_ADMIN)])

def get_department_by_user_id(user_id: int, lang: str) -> str:
    users_of_department = get_package_by_lang(lang=lang).departments

    for key, dep in users_of_department.items():
        for user in dep.list_of_employees:
            if user.tg_id == user_id:
                return dep.name
    
    return Employee(name="Unknown", tg_id=SUPER_ADMIN)
        

def  get_employee_name_by_id(user_id: int, lang: str) -> str:
    users_of_department = get_package_by_lang(lang=lang).departments
    
    for key, dep in users_of_department.items():
        for employee in dep.list_of_employees:
            if employee.tg_id == user_id:
                return employee.name, dep.name
    
    if user_id == SUPER_ADMIN:
        return "Super Admin", "Super Department"
    
    return None, None



def is_admin(user_id: int) -> bool:
    for key, value in departments.items():
        for employee in value.list_of_employees:
            if employee.tg_id == user_id:
                return True            

    if user_id == SUPER_ADMIN:
        return True

    return False
