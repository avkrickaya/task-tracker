# app/schemas/task.py
# Схемы для задач

from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.task import TaskPriority, TaskStatus  # импорт Enum-типов из модели

# Базовая схема — поля, которые используются при создании/обновлении
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: TaskPriority = TaskPriority.medium
    status: TaskStatus = TaskStatus.todo
    start_date: Optional[datetime] = None
    due_date: Optional[datetime] = None
    sprint_id: Optional[int] = None
    category_id: Optional[int] = None

# Схема для создания — пока просто TaskBase
class TaskCreate(TaskBase):
    pass

# Схема для ответа клиенту — добавляем id и created_at
class TaskOut(TaskBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True  # позволяет возвращать ORM-объекты напрямую
