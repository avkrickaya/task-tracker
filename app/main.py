# точка входа приложения
from fastapi import FastAPI
from app.database import Base, engine
from app.routes import task

# создание таблиц, если их еще нет
Base.metadata.create_all(bind=engine)

# создание FastAPI-приложение
app = FastAPI(title="Task Tracker")

# подключение роуты
app.include_router(task.router)