# app/schemas/habit_log.py
from pydantic import BaseModel
from datetime import date
from typing import Optional

class HabitLogBase(BaseModel):
    habit_id: int
    date: date
    value: Optional[int] = None
    done: Optional[bool] = True

class HabitLogCreate(HabitLogBase):
    pass

class HabitLogOut(HabitLogBase):
    id: int

    class Config:
        orm_mode = True
