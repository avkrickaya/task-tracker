from fastapi import APIRouter
from pydantic import BaseModel

router =APIRouter()

# --- Наш список задач ---
tasks = [
    {"id": 1, "title": "Купить продукты", "done": False},
    {"id": 2, "title": "Сделать зарядку", "done": True}
]

class Task(BaseModel):
    title: str
    done: bool =False

@router.get("/tasks")
def get_tasks():
    return tasks

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Задача не найдена"}

@router.post("/tasks")
def add_task(task: Task):
    mew_task = {"id": len(tasks) + 1, "title": task.title, "done": task.done}
    tasks.append(new_task)
    return new_task

