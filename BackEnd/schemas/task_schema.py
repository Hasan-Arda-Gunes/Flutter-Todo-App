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
    user_id: str

    class Config:
        orm_mode = True

class TaskSearch(BaseModel):
    title: str