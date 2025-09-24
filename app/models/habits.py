from pydantic import BaseModel, Field
from datetime import date
from typing import List

class Habit(BaseModel):
    id: int
    name: str = Field(min_length=3, max_length=50)
    frequency: str = Field(pattern="^(ежедневно|еженедельно|ежемесячно)$")
    active: bool = True

class HabitCreate(BaseModel):
    name: str
    frequency: str

class HabitLog(BaseModel):
    id: int 
    date: date