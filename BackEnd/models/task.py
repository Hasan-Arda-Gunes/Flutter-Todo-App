from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from database import Base
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), index=True, nullable=False)
    isDone = Column(Boolean, nullable=False)
    priority = Column(Integer, nullable=False)
    due_date = Column(DateTime, nullable=True)
    user_id = Column(String(255), ForeignKey("users.username"))
    user = relationship("User", back_populates="tasks")