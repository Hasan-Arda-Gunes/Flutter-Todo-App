from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.task_schema import TaskCreate, TaskSearch, TaskResponse
from service.task_service import create_task_service, delete_task_service, toggle_task
from repository.task_repository import get_tasks_by_user
from database import get_db
from models import User
from auth import get_current_user
from typing import List

router = APIRouter(
    dependencies=[Depends(get_current_user)]
)

@router.post("/create")
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    try:
        new_task = create_task_service(db, task, current_user)
        new_task.user_id = current_user.username
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.post("/delete")
def delete_task(task: TaskSearch, db: Session = Depends(get_db)):
    success = delete_task_service(db, task)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return None

@router.post("/toggle")
def update_task(task: TaskSearch, db: Session = Depends(get_db)):
    success = toggle_task(db, task)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return None

@router.get("/get",response_model=List[TaskResponse])
def get_user_tasks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_tasks_by_user(db, current_user.username)

