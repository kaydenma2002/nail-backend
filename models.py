from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.sql import text

from db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String(50))
    first_name = Column(String(50))
    address = Column(String(50))
    email = Column(String(100), unique=True, index=True, nullable=False, server_default=text("''")) 
    password = Column(String(1000))

class Nail(Base):
    __tablename__ = 'nails'
    id = Column(Integer, primary_key=True, index=True)
    title= Column(String(50))
    content = Column(String(100))
    address = Column(String(100))
    user_id = Column(Integer)