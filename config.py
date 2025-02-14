from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_url = "sqlite:///todo.db"
engine = create_engine(db_url, connect_args={"check_same_thread": False})

Base = declarative_base()
from models.user import User
from models.board import Board
from models.task import Task
from models.category import Category

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()