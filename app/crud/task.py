# функция для работы с задачами (CRUD)
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate

# получить все задачи
def get_tasks(db: Session):
    return db.query(Task).all()

# получить задачу по id
def get_task(db: Session, task_id: int):
    return db.query(Task). filter(Task.id == task_id).first()

# создать задачу
def create_task(db: Session, task: TaskCreate):
    db_task = task(**task.dict()) # распаковка dict из Pydantic-модели
    db.add(db_task)
    db.commit()
    db.refresh(db_task) # обновление объекта (чтобы был id)
    return db_task