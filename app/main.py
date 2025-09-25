# app/main.py
# Запуск приложения и регистрация роутов

from fastapi import FastAPI
from app.database import Base, engine

# импортируем роутеры
from app.routes import tasks, sprints, categories, habits, habit_logs, analytics

# импорт моделей нужен, чтобы SQLAlchemy "увидел" все модели при создании таблиц
# (в некоторых случаях достаточно импорта модулей, поэтому мы импортируем их)
from app.models import task, sprint, category, habit, habit_log  

# создаём все таблицы (если не существуют)
Base.metadata.create_all(bind=engine)

# создаём экземпляр FastAPI
app = FastAPI(title="Task & Habit Tracker")

# регистрируем роутеры
app.include_router(tasks.router)
app.include_router(sprints.router)
app.include_router(categories.router)
app.include_router(habits.router)
app.include_router(habit_logs.router)
app.include_router(analytics.router)
