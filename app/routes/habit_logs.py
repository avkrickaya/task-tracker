# app/routes/habit_logs.py
# Эндпоинты для создания/просмотра логов привычек

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.habit_log import HabitLogCreate, HabitLogOut
from app.crud.habit_log import create_habit_log, get_habit_logs_for_habit
from app.crud.habit import get_habit

router = APIRouter(prefix="/habit-logs", tags=["habit_logs"])

@router.post("/", response_model=HabitLogOut)
def add_habit_log(log_in: HabitLogCreate, db: Session = Depends(get_db)):
    """
    Добавить запись выполнения привычки.
    Если запись на эту дату уже есть, логика: сейчас мы просто создаем ещё одну запись.
    (Можно добавить уникальность habit_id+date в модели, если нужно.)
    """
    # проверяем, что привычка существует
    if not get_habit(db, log_in.habit_id):
        raise HTTPException(status_code=404, detail="Habit not found")
    return create_habit_log(db, log_in)

@router.get("/habit/{habit_id}", response_model=List[HabitLogOut])
def get_logs_for_habit(habit_id: int, db: Session = Depends(get_db)):
    """Вернуть все логи для привычки."""
    if not get_habit(db, habit_id):
        raise HTTPException(status_code=404, detail="Habit not found")
    return get_habit_logs_for_habit(db, habit_id)
