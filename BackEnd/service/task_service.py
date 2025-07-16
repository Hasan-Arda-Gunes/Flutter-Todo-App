from sqlalchemy.orm import Session
from repository import task_repository
from schemas.task_schema import TaskCreate, TaskSearch
from models import Task, User


def create_task_service(db: Session, task_data: TaskCreate, current_user: User) -> Task:
    new_task = Task(
        title=task_data.title,
        priority=task_data.priority,
        due_date=task_data.due_date,
        isDone=False, 
        user_id=current_user.username
    )
    return task_repository.create_task(db, new_task)


def toggle_task(db: Session, task: TaskSearch) -> Task:
    task = task_repository.get_task_by_id(db, task.id)
    if task:
        task.isDone = not task.isDone
        db.commit()
        db.refresh(task)
        return True
    return False

def delete_task_service(db: Session, task: TaskSearch) -> bool:
    task = task_repository.get_task_by_id(db, task.id)
    if task:
        db.delete(task)
        db.commit()
        return True
    return False