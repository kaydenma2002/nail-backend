from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.user import UserService
from db import get_db
from schemas.user import UserBase, LoginData
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

@router.post("/create-user/")
async def create_user(user: UserBase, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.create_user(user)
@router.post("/authenticate-user/")
async def authenticate_user(LoginData: LoginData, db: Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.authenticate_user(LoginData)
@router.post("/get-user/")
async def get_current_user(db: Session = Depends(get_db),token:str = Depends(oauth2_scheme)):
    user_service = UserService(db)
    return user_service.get_current_user(token)
@router.get("/protected")
async def protected_route(current_user: UserBase = Depends(get_current_user)):
    return {"message": "This is a protected route", "user": current_user}
    
@router.get("/connect-to-dropbox")
async def connect_to_dropbox(db: Session = Depends(get_db), access_token: str = None):
    user_service = UserService(db)
    result = await user_service.connect_to_dropbox(access_token,"KAYDEN/nail/1/1.jpg")
    return result