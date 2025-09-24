from fastapi import APIRouter
from app.models.habits import Habit, HabitCreate, HabitLog
from datetime import date

router = APIRouter()

# Временное хранилище в памяти
habits_db: list[Habit] = []
habit_logs: list[HabitLog] = []
id_counter = 1

@router.get("/habits", response_model=list[Habit])
def get_habits():
    return habits_db

@router.post("/habits", response_model=Habit)
def create_habit(habit: HabitCreate):
    global id_counter
    new_habit = Habit(id=id_counter, name=habit.name, frequency=habit.frequency, active=True)
    habits_db.append(new_habit)
    id_counter += 1
    return new_habit

@router.post("/habits/log")
def log_habit(log: HabitLog):
    habit_logs.append(log)
    return {"message": "Привычка отмечена!", "log": log}