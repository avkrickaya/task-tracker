# app/models/habit.py
# Модель привычки (Habit)

from sqlalchemy import Column, Integer, String, Boolean, Enum
from sqlalchemy.orm import relationship
import enum

from app.database import Base

# Enum для частоты привычки (daily/weekly/custom)
class HabitFrequency(str, enum.Enum):
    daily = "daily"
    weekly = "weekly"
    custom = "custom"

class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)     # id привычки
    name = Column(String, nullable=False)                  # название привычки
    description = Column(String, nullable=True)            # описание
    frequency = Column(Enum(HabitFrequency), default=HabitFrequency.daily)  # частота
    goal = Column(Integer, nullable=True)                  # числовая цель (например, стаканов воды)
    is_active = Column(Boolean, default=True)              # активна ли привычка

    # связь: привычка имеет множество логов
    logs = relationship("HabitLog", back_populates="habit")
