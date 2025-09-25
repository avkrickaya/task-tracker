from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from app.models.task import Task, TaskStatus
from app.models.habit import Habit
from app.models.habit_log import HabitLog

# ---------- АНАЛИТИКА ПО ЗАДАЧАМ ----------

def get_task_stats(db: Session, days: int = 7):
    """
    Возвращает словарь с количеством задач:
    - всего
    - выполненных
    - в работе
    - запланированных
    """
    start_date = datetime.utcnow() - timedelta(days=days)
    total = db.query(func.count(Task.id)).filter(Task.created_at >= start_date).scalar()
    done = db.query(func.count(Task.id)).filter(Task.created_at >= start_date, Task.status == TaskStatus.done).scalar()
    in_progress = db.query(func.count(Task.id)).filter(Task.created_at >= start_date, Task.status == TaskStatus.in_progress).scalar()
    todo = db.query(func.count(Task.id)).filter(Task.created_at >= start_date, Task.status == TaskStatus.todo).scalar()

    return {
        "total": total,
        "done": done,
        "in_progress": in_progress,
        "todo": todo,
        "completion_rate": (done / total * 100) if total > 0 else 0
    }

def get_task_by_category(db: Session):
    results = db.query(Task.category_id, func.count(Task.id)).group_by(Task.category_id).all()
    return [{"category_id": c, "count": cnt} for c, cnt in results]

def get_task_by_priority(db: Session):
    results = db.query(Task.priority, func.count(Task.id)).group_by(Task.priority).all()
    return [{"priority": p.value, "count": cnt} for p, cnt in results]


# ---------- АНАЛИТИКА ПО ПРИВЫЧКАМ ----------

def get_habit_stats(db: Session, days: int = 30):
    """
    Аналитика по привычкам: общее количество, выполненные за период, % успеха.
    """
    start_date = datetime.utcnow() - timedelta(days=days)
    total_logs = db.query(func.count(HabitLog.id)).filter(HabitLog.date >= start_date).scalar()
    completed = db.query(func.count(HabitLog.id)).filter(HabitLog.date >= start_date, HabitLog.done == True).scalar()

    return {
        "total_logs": total_logs,
        "completed": completed,
        "success_rate": round((completed / total_logs * 100), 2) if total_logs > 0 else 0
    }

def get_habit_by_category(db: Session):
    results = db.query(Habit.category_id, func.count(Habit.id)).group_by(Habit.category_id).all()
    return [{"category_id": c, "count": cnt} for c, cnt in results]

def get_habit_streaks(db: Session):
    """
    Возвращает длину самой длинной серии подряд выполнений для каждой привычки.
    (Упрощенный вариант — пока просто количество выполнений)
    """
    results = db.query(Habit.id, func.count(HabitLog.id)).join(HabitLog).filter(HabitLog.done == True).group_by(Habit.id).all()
    return [{"habit_id": h, "streak": cnt} for h, cnt in results]
