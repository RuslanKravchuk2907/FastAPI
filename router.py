from typing import Annotated

from fastapi import APIRouter, Depends
from reposetory import TaskReposetory

from schemas import STaskAdd, STask, STaskId

router = APIRouter(prefix="/tasks")


@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskReposetory.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> STask:
    tasks = await TaskReposetory.find_all()
    return tasks
