from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from database import Base
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, index=True)
    isDone = Column(Boolean, nullable=False)
    user_id = Column(String(255), ForeignKey("users.username"))
    user = relationship("User", back_populates="tasks")