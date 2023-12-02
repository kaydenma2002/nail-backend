from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.user import UserService
from db import get_db
from schemas.user import UserBase, LoginData
from security import  reusable_oauth2

router = APIRouter()

@router.post("/create-user/")
async def create_user(user: UserBase, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.create_user(user)
@router.post("/authenticate-user/")
async def authenticate_user(LoginData: LoginData, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.authenticate_user(LoginData)
@router.get('/books', dependencies=[Depends(reusable_oauth2)])
def list_books():
    return {'data': ['Sherlock Homes', 'Harry Potter', 'Rich Dad Poor Dad']}
