# app/models/habit_log.py
# Модель записи выполнения привычки (HabitLog)

from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class HabitLog(Base):
    __tablename__ = "habit_logs"

    id = Column(Integer, primary_key=True, index=True)       # id лога
    habit_id = Column(Integer, ForeignKey("habits.id"), nullable=False)  # ссылка на привычку
    date = Column(Date, nullable=False)                       # дата выполнения
    value = Column(Integer, nullable=True)                    # числовое значение (например, количество стаканов)
    done = Column(Boolean, default=True)                      # факт выполнения (True/False)

    # ORM-связь к привычке
    habit = relationship("Habit", back_populates="logs")
