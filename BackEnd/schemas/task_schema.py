from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    priority: int
    due_date: Optional[datetime] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    isDone: bool
    priority: int
    due_date: datetime | None
    user_id: str

    class Config:
        from_attributes = True

class TaskSearch(BaseModel):
    id: int