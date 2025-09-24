# Модель задачи в БД
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from app.database import Base # базовый класс моделей

# создание Enum для приоритетов
class TaskPriority(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

# созданием Enum для статуса
class TaskStatus(str, enum.Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

# Модель задачи
class Task(Base):
    __tablename__ = "tasks" # имя таблицы в БД

    id = Column(Integer, primary_key=True, index=True) # уникальный ID
    title = Column(String, nullable=False) # название задачи
    description = Column(String, nullable=True) # описание
    priority = Column(Enum(TaskPriority), default=TaskPriority.medium) # приоритет
    status = Column(Enum(TaskStatus), default=TaskStatus.todo) # статус
    created_at = Column(DateTime, default=datetime.utcnow) # дата создания
    start_date = Column(DateTime, nullable=True) # Дата начала
    due_date = Column(DateTime, nullable=True) # дедлайн
    completed_at = Column(DateTime, nullable=True) # дата завершения

# связи (FK)
sprint_id = Column(Integer, ForeignKey("sprints.id"), nullable=True)
category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)

# связи ORM - чтобы можно было получить sprint / category через task.sprint
sprint = relationship("Sprint", back_populates="tasks")
category = relationship("Category", back_populates="tasks")
