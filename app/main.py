from fastapi import FastAPI

# Создание приложения
app = FastAPI()

# Простой маршрут (endpoint)
@app.get("/")
def read_root():
    return {"message": "Task Tracker работает!"}

# Маршрут для проверки, что сервер живой
@app.get("/ping")
def ping():
    return {"status": "ok"}