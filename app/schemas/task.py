# Pydantic-модели для валидации запросов/ответов
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.task import TaskPriority, TaskStatus

# базовая схема задачи (чтение + запись)
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    priority: TaskPriority = TaskPriority.medium
    status: TaskStatus = TaskStatus.todo
    start_date: Optional[datetime] = None
    due_date: Optional[datetime] = None

# для создания задачи (нет id)
class TaskCreate(TaskBase):
    pass 

# для возврата клиенту (id добавлен)
class TaskOut(TaskBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True # нужно, чтобы Pydantic  мог работать с ORM объектами