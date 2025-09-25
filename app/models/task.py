# app/models/task.py
# Модель задачи (Task)

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum  # столбцы типов
from sqlalchemy.orm import relationship  # для связи ORM-объектов
from datetime import datetime
import enum

from app.database import Base  # базовый класс моделей из database.py

# Enum (Python) для приоритета задачи
class TaskPriority(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"

# Enum (Python) для статуса задачи
class TaskStatus(str, enum.Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"

# SQLAlchemy-модель таблицы tasks
class Task(Base):
    __tablename__ = "tasks"                          # имя таблицы в БД

    id = Column(Integer, primary_key=True, index=True)  # первичный ключ, индексируем
    title = Column(String, nullable=False)              # заголовок задачи (обязательное поле)
    description = Column(String, nullable=True)         # описание задачи (необязательное)
    priority = Column(Enum(TaskPriority), default=TaskPriority.medium)  # приоритет из Enum
    status = Column(Enum(TaskStatus), default=TaskStatus.todo)         # статус из Enum
    created_at = Column(DateTime, default=datetime.utcnow)  # время создания
    start_date = Column(DateTime, nullable=True)           # когда нужно начать
    due_date = Column(DateTime, nullable=True)             # дедлайн
    completed_at = Column(DateTime, nullable=True)         # когда завершили

    # Внешние ключи на спринт и категорию (опционально)
    sprint_id = Column(Integer, ForeignKey("sprints.id"), nullable=True)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)

    # ORM-связи: даём имена атрибутам для обратной навигации
    sprint = relationship("Sprint", back_populates="tasks")
    category = relationship("Category", back_populates="tasks")

