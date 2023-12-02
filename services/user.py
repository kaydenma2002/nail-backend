from sqlalchemy.orm import Session
from models import User
from schemas.user import UserBase, LoginData
from datetime import datetime, timedelta
from typing import Union, Any
from fastapi import FastAPI, HTTPException
import bcrypt
import jwt

SECURITY_ALGORITHM = 'HS256'
SECRET_KEY = '123456'
class UserService:
    def __init__(self, db: Session):
        
        self.db = db
    def create_user(self, user: UserBase):
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

        # Store the hashed password in the User model
        db_user = User(
            email=user.email,
            password=hashed_password.decode('utf-8')
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    @staticmethod
    def generate_token(email: str):
        expire = datetime.utcnow() + timedelta(
        seconds=60 * 60 * 24 * 3  # Expired after 3 days
        )
        to_encode = {
            "exp": expire, "email": email
        }
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=SECURITY_ALGORITHM)
        return encoded_jwt
    def authenticate_user(self, login_data: LoginData):
        user = self.db.query(User).filter(User.email == login_data.email).first()
        if user and bcrypt.checkpw(login_data.password.encode('utf-8'), user.password.encode('utf-8')):
            token = self.generate_token(login_data.email)
            return {
                'token': token
            }
        else:
            return False
    
    

    
    
    
