# app/schemas/habit.py
from pydantic import BaseModel
from typing import Optional
from app.models.habit import HabitFrequency

class HabitBase(BaseModel):
    name: str
    description: Optional[str] = None
    frequency: HabitFrequency = HabitFrequency.daily
    goal: Optional[int] = None
    is_active: bool = True

class HabitCreate(HabitBase):
    pass

class HabitOut(HabitBase):
    id: int

    class Config:
        orm_mode = True
