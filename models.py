from sqlalchemy import Boolean, Column, Integer, String,ForeignKey
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship

from db import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String(50))
    first_name = Column(String(50))
    address = Column(String(50))
    email = Column(String(100), unique=True, index=True, nullable=False, server_default=text("''")) 
    password = Column(String(1000))
    nails = relationship("Nail", back_populates="owner")
class Nail(Base):
    __tablename__ = 'nails'
    id = Column(Integer, primary_key=True, index=True)
    name= Column(String(50))
    full_address = Column(String(100))
    street_address = Column(String(100))
    city = Column(String(100))
    state = Column(String(100))
    postal_code = Column(String(100))
    phone = Column(String(100))
    categories = Column(String(100))
    user_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship("User", back_populates="nails")
    

