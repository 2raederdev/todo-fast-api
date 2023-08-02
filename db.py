from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args = {"check_same_thread": False})

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Boolean, ARRAY
class Items(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(50), unique=True)
    description = Column(String(200))
    is_done = Column(Boolean)

    Base.metadata.create_all(bind=engine)

