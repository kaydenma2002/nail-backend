from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.user import UserService
from db import get_db
from schemas.user import UserBase

router = APIRouter()

@router.post("/create-user/")
async def create_user(user: UserBase, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.create_user(user)
@router.post("/authenticate-user/")
async def authenticate_user(email,password, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.authenticate_user(email,password)

