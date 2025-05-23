from __future__ import annotations
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import types
from dataclasses import dataclass
from typing import List, Optional

class MurojaatStates(StatesGroup):
    step_one = State() # Murojaat qiluvchi kimligini tanlash
    step_two = State() # Murojaat maqsadi tugmasi bosilganda
    step_three = State() # Murojaat kimga yuborilishi kerak tugmasi bosilganda
    step_four = State() # Ism Familiya
    step_five = State() # Telefon raqami
    step_six = State() # Murojaat matni
    step_seven = State() # Murojaatni tasdiqlash


class AdminStates(StatesGroup):
    admin = State()


@dataclass
class Employee:
    name: str
    tg_id : int

@dataclass
class Department:
    name: str
    list_of_employees: Optional[List[Employee]] = None




