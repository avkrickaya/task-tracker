# app/routes/habits.py
# Эндпоинты для привычек

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date, timedelta, datetime

from app.database import get_db
from app.schemas.habit import HabitCreate, HabitOut
from app.crud.habit import get_habits, get_habit, create_habit
from app.crud.habit_log import get_habit_logs_in_period

router = APIRouter(prefix="/habits", tags=["habits"])

@router.get("/", response_model=List[HabitOut])
def read_habits(db: Session = Depends(get_db)):
    """Вернуть все привычки."""
    return get_habits(db)

@router.get("/{habit_id}", response_model=HabitOut)
def read_habit(habit_id: int, db: Session = Depends(get_db)):
    habit = get_habit(db, habit_id)
    if not habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    return habit

@router.post("/", response_model=HabitOut)
def create_new_habit(habit_in: HabitCreate, db: Session = Depends(get_db)):
    """Создать привычку."""
    return create_habit(db, habit_in)

@router.get("/{habit_id}/logs")
def habit_logs(habit_id: int, 
               days: Optional[int] = Query(None, description="количество дней назад от today"),
               db: Session = Depends(get_db)):
    """
    Пример: /habits/1/logs?days=30  — вернуть логи за последние 30 дней
    Если days не указан — вернуть все логи.
    """
    date_from = None
    date_to = None
    if days is not None:
        date_to = datetime.utcnow().date()
        date_from = date_to - timedelta(days=days)
    logs = get_habit_logs_in_period(db, habit_id, date_from, date_to)
    return logs
