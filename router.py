from typing import Annotated

from fastapi import APIRouter, Depends
from reposetory import TaskReposetory

from schemas import STaskAdd


router = APIRouter(prefix="/tasks")


@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
):
    task_id = await TaskReposetory.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks():
    tasks = await TaskReposetory.find_all()
    return {"tasks": tasks}
