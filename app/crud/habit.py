# app/crud/habit.py

from sqlalchemy.orm import Session
from app.models.habit import Habit
from app.schemas.habit import HabitCreate

def get_habits(db: Session):
    """Вернуть все привычки."""
    return db.query(Habit).all()

def get_habit(db: Session, habit_id: int):
    """Вернуть привычку по id."""
    return db.query(Habit).filter(Habit.id == habit_id).first()

def create_habit(db: Session, habit_in: HabitCreate):
    """Создать привычку."""
    db_habit = Habit(**habit_in.dict())
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit
