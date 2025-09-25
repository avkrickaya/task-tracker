# app/routes/analytics.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
# Импортируем CRUD-функции для задач и привычек
from app.crud.analytics import (
    get_task_stats, get_task_by_category, get_task_by_priority,
    get_habit_stats, get_habit_by_category, get_habit_streaks
)

# Создаём роутер для всей аналитики
router = APIRouter()

# ---------- АНАЛИТИКА ПО ЗАДАЧАМ ----------

@router.get("/analytics/tasks")
def analytics_tasks(period: int = 7, db: Session = Depends(get_db)):
    """
    Возвращает аналитику по задачам за последние N дней.
    """
    return get_task_stats(db, days=period)

@router.get("/analytics/tasks/categories")
def analytics_task_categories(db: Session = Depends(get_db)):
    """
    Количество задач по категориям.
    """
    return get_task_by_category(db)

@router.get("/analytics/tasks/priorities")
def analytics_task_priorities(db: Session = Depends(get_db)):
    """
    Количество задач по приоритетам.
    """
    return get_task_by_priority(db)


# ---------- АНАЛИТИКА ПО ПРИВЫЧКАМ ----------

@router.get("/analytics/habits")
def analytics_habits(period: int = 30, db: Session = Depends(get_db)):
    """
    Возвращает аналитику по привычкам (количество выполнений, % успеха) за N дней.
    """
    return get_habit_stats(db, days=period)

@router.get("/analytics/habits/categories")
def analytics_habit_categories(db: Session = Depends(get_db)):
    """
    Количество привычек по категориям.
    """
    return get_habit_by_category(db)

@router.get("/analytics/habits/streaks")
def analytics_habit_streaks(db: Session = Depends(get_db)):
    """
    Возвращает streak (длину серии подряд выполнений) по каждой привычке.
    """
    return get_habit_streaks(db)
