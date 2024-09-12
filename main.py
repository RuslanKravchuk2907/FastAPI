from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class STaskAdd(BaseModel):
    name: str
    description: str | None


class Stask(STaskAdd):


@app.get("/tasks")
def get_tasks():
    task = Task(name="Не забувай практикуватися")
    return {"data": task}
