from typing import Optional, Annotated

from fastapi import FastAPI
from pydantic import BaseModel

from contextlib import asynccontextmanager

from DataBase import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Base is clear")
    await create_tables()
    print("Base is ready")
    yield
    print("Off")

app = FastAPI(lifespan=lifespan)


class STaskAdd(BaseModel):
    name: str
    description: str | None


class STask(STaskAdd):
    id: int

tasks = []


@app.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
):
    tasks.append(task)
    return {"ok": True}



#@app.get("/tasks")
#def get_tasks():
#    task = Task(name="Не забувай практикуватися")
#    return {"data": task}
