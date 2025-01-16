from typing import List

from fastapi import APIRouter, HTTPException
from regex import R
from models.task import Task
from dal.repositories.task_repository import TaskRepository

from dal.dal import RepositoryFactory

router = APIRouter()
task_repository: TaskRepository = RepositoryFactory.get_repository(TaskRepository)

@router.get("/tasks", response_model=List[Task])
def get_tasks():
    return task_repository.get_all()

@router.get("/task/get/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = task_repository.get_by_id(task_id)
    if task:
        return task
    else:
        raise HTTPException(status_code=404, detail="Task not found")

@router.post("/task/create", response_model=None)
def create_task(task: Task):
    created = task_repository.create(task)
    if created:
        raise HTTPException(status_code=201, detail="Task created")
    else:
        raise HTTPException(status_code=400, detail="Task already exists")


@router.put("/task/update", response_model=None)
def update_task(updated_task: Task):
    updated = task_repository.update(updated_task)
    if updated:
        raise HTTPException(status_code=204, detail="Task updated")
    else:
        raise HTTPException(status_code=400, detail="Task not found")


@router.delete("/task/delete/{task_id}", response_model=None)
def delete_task(task_id: int):
    deleted = task_repository.delete(task_id)
    if deleted:
        raise HTTPException(status_code=204, detail="Task deleted")
    else:
        raise HTTPException(status_code=400, detail="Task not found")
