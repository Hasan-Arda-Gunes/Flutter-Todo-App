from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    username = Column(String(255), primary_key=True, index=True)
    password = Column(String(255), nullable=False)
    tasks = relationship("Task", back_populates="user")
