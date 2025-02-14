from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from config import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    priority = Column(String, default="Medium")
    category_id = Column(Integer, ForeignKey("categories.id"))
    board_id = Column(Integer, ForeignKey("boards.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    category = relationship("Category")
    board = relationship("Board")
    user = relationship("User")
