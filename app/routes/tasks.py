# app/routes/tasks.py
# Эндпоинты для задач

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database import get_db
from app.schemas.task import TaskCreate, TaskOut, TaskBase
from app.crud.task import get_tasks, get_task, create_task, update_task, delete_task
from app.models.task import Task as TaskModel  # модель для фильтров

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=List[TaskOut])
def read_tasks(
    category_id: Optional[int] = Query(None),  # ?category_id=1
    sprint_id: Optional[int] = Query(None),    # ?sprint_id=2
    db: Session = Depends(get_db)
):
    """
    Вернуть список задач. Опционально фильтровать по category_id или sprint_id.
    """
    # начинаем запрос от модели Task
    q = db.query(TaskModel)
    if category_id is not None:
        q = q.filter(TaskModel.category_id == category_id)
    if sprint_id is not None:
        q = q.filter(TaskModel.sprint_id == sprint_id)
    return q.all()

@router.get("/{task_id}", response_model=TaskOut)
def read_task(task_id: int, db: Session = Depends(get_db)):
    """
    Вернуть задачу по id.
    """
    db_task = get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.post("/", response_model=TaskOut)
def create_new_task(task_in: TaskCreate, db: Session = Depends(get_db)):
    """
    Создать новую задачу.
    """
    return create_task(db, task_in)

@router.patch("/{task_id}", response_model=TaskOut)
def patch_task(task_id: int, updates: TaskBase, db: Session = Depends(get_db)):
    """
    Частичное обновление задачи: передать поля, которые нужно изменить.
    (TaskBase — все поля optional в Pydantic? здесь TaskBase не optional.
    Для полной частичной модели можно создать TaskUpdate с Optional-полями;
    но для простоты используем dict(exclude_unset=True) ниже.)
    """
    db_task = get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    # берём только переданные поля (exclude_unset) — чтобы не затирать поля дефолтами
    updates_dict = updates.dict(exclude_unset=True)
    updated = update_task(db, db_task, updates_dict)
    return updated

@router.delete("/{task_id}")
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    """
    Удалить задачу.
    """
    db_task = get_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    delete_task(db, db_task)
    return {"ok": True}
