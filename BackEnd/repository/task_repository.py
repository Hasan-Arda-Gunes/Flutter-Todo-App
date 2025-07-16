from sqlalchemy.orm import Session
from models import Task
from typing import List, Optional


def get_task_by_id(db: Session, id: int) -> Optional[Task]:
    return db.query(Task).filter(Task.id == id).first()

def create_task(db: Session, task: Task):
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks_by_user(db: Session, user_id: str) -> List[Task]:
    return db.query(Task).filter(Task.user_id == user_id).all()

def get_task_by_title(db: Session, title: str) -> Optional[Task]:
    return db.query(Task).filter(Task.title == title).first()


