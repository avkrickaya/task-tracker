# app/models/sprint.py
# Модель спринта (Sprint)

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base  # базовый класс моделей

class Sprint(Base):
    __tablename__ = "sprints"  # имя таблицы

    id = Column(Integer, primary_key=True, index=True)  # id спринта
    name = Column(String, nullable=False)               # название спринта
    start_date = Column(DateTime, default=datetime.utcnow)  # дата начала
    end_date = Column(DateTime, nullable=True)               # дата окончания

    # связь "один ко многим": один спринт -> много задач
    tasks = relationship("Task", back_populates="sprint")

