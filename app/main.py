from fastapi import FastAPI
from pydantic import BaseModel
from app.routes import habits, tasks

# Создание приложения
app = FastAPI()

# Регистрируем роутеры
app.include_router(tasks.router)
app.include_router(habits.router)

