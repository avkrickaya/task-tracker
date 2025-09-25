# app/crud/task.py
# CRUD для задач

from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate

def get_tasks(db: Session):
    """Вернуть все задачи."""
    return db.query(Task).all()

def get_task(db: Session, task_id: int):
    """Вернуть задачу по ID (или None)."""
    return db.query(Task).filter(Task.id == task_id).first()

def create_task(db: Session, task_in: TaskCreate):
    """Создать задачу из Pydantic-модели TaskCreate."""
    db_task = Task(**task_in.dict())  # распаковка словаря в конструктор модели
    db.add(db_task)                  # добавляем в сессию
    db.commit()                      # коммитим (сохраняем)
    db.refresh(db_task)              # обновляем объект (чтобы получить id и т.д.)
    return db_task

def update_task(db: Session, db_task: Task, updates: dict):
    """Частичное обновление: передаём существующий объект и dict с изменениями."""
    for key, value in updates.items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, db_task: Task):
    """Удалить задачу из базы."""
    db.delete(db_task)
    db.commit()
    return
