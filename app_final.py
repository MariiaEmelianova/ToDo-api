import os
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

APP_NAME = os.getenv("APP_NAME", "To-Do List Service")
APP_AUTHOR = os.getenv("APP_AUTHOR", "Person")
MAX_TASKS = int(os.getenv("MAX_TASKS", "10"))

app = FastAPI(title=APP_NAME)

tasks_db = []

class TaskCreate(BaseModel):
    title: str
    description: str = ""
    completed: bool = False

@app.get("/")
def root():
    logger.info("Запрос к корневому маршруту")
    return {"message": f'{APP_NAME} is running'}

@app.get("/health")
def health_check():
    logger.info("Проверка здоровья сервиса")
    return {"status": "ok"}


@app.get("/version")
def get_version():
    logger.info("Запрос версии приложения")
    return {"version": "1.0.0", "author": APP_AUTHOR}


@app.get("/info")
def info():
    logger.info("Запрос информации о приложении")
    return {"name": APP_NAME, "author": APP_AUTHOR}

@app.post("/tasks")
def create_task(task: TaskCreate):
    if len(tasks_db) >= MAX_TASKS:
        logger.warning(f'Отклонено: превышен лимит задач ({MAX_TASKS}')
        raise HTTPException(status_code=400, detail=f'Достигнут лимит: {MAX_TASKS} задач')

    task_dict = task.model_dump()
    task_dict["id"] = len(tasks_db) + 1
    tasks_db.append(task_dict)
    logger.info(f"Создана задача ID={task_dict['id']}: {task.title}")
    return task_dict

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    logger.info(f'Запрос задачи ID={task_id}')
    for t in tasks_db:
        if t['id'] == task_id:
            return t
    logger.error(f'Задача ID={task_id} не найдена')
    raise HTTPException(status_code=404, detail="Задача не найдена")

@app.get("/tasks", response_model=List[TaskCreate])
def get_all_tasks():
    return tasks_db

@app.patch("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    for t in task_db:
        if t['id'] == task_id:
            t['completed'] = True
            logger.info(f'Задача ID={task_id} выполнена')
            return {'massage': "Задача выполнена", 'task': t}
    raise HTTPException(status_code=404, detail="Задача не найдена")

