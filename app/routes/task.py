# эндпоинты FastAPI для задач
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.task import TaskCreate, TaskOut
from app.crud.task import get_tasks, get_task, create_task

router = APIRouter()

@router.get("/tasks", response_model=List[TaskOut])
def read_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)

@router.get("/tasks/{task_id}", response_model=TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    return get_task(db, task_id)

@router.post("/tasks", response_model=TaskOut)
def add_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)