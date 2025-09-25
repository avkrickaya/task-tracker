# app/crud/habit_log.py

from sqlalchemy.orm import Session
from app.models.habit_log import HabitLog
from app.schemas.habit_log import HabitLogCreate
from datetime import date

def create_habit_log(db: Session, log_in: HabitLogCreate):
    """Добавить запись выполнения привычки."""
    db_log = HabitLog(**log_in.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

def get_habit_logs_for_habit(db: Session, habit_id: int):
    """Получить все логи для привычки."""
    return db.query(HabitLog).filter(HabitLog.habit_id == habit_id).order_by(HabitLog.date.desc()).all()

def get_habit_logs_in_period(db: Session, habit_id: int, date_from, date_to):
    """Получить логи привычки за период (включительно)."""
    q = db.query(HabitLog).filter(HabitLog.habit_id == habit_id)
    if date_from is not None:
        q = q.filter(HabitLog.date >= date_from)
    if date_to is not None:
        q = q.filter(HabitLog.date <= date_to)
    return q.order_by(HabitLog.date.asc()).all()
