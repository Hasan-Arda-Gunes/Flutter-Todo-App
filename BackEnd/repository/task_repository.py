from sqlalchemy.orm import Session
from models import Task


def get_task_by_id(db: Session, id: int):
    return db.query(Task).filter(Task.id == id).first()

def create_task(db: Session, task: Task):
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


