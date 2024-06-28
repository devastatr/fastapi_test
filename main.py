from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    name: str
    deck: Optional[str] = None


@app.get("/tasks")
def get_tasks():
    task = Task(name="Тестовое задание")
    return {"data": task}
