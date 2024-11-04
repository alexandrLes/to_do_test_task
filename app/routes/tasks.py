from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas import TaskCreate, TaskUpdate, TaskInDB
from app.crud import create_task, get_task, update_task, get_tasks
from app.database import get_db
from app.auth import get_current_user

router = APIRouter()

@router.post("/tasks/create", response_model=TaskInDB, status_code=status.HTTP_201_CREATED)
def create_task_endpoint(task: TaskCreate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    """Create a new task with `datetime_to_do` and `task_info`."""
    return create_task(db, task)

@router.get("/tasks/{task_id}", response_model=TaskInDB)
def get_task_endpoint(task_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    """Retrieve a specific task by `task_id`."""
    db_task = get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return db_task

@router.patch("/tasks/{task_id}/update", response_model=TaskInDB)
def update_task_endpoint(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    """Update `datetime_to_do` and `task_info` for a specific task."""
    db_task = update_task(db, task_id, task_update)
    if db_task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return db_task

@router.get("/tasks/list", response_model=List[TaskInDB])
def list_tasks_endpoint(db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    """Retrieve a list of all tasks."""
    return get_tasks(db)
