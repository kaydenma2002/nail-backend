from fastapi import Depends, APIRouter, Query, Depends
from sqlalchemy.orm import Session
from services.nail import NailService
from db import get_db
from schemas.nail import NailBase
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
router = APIRouter()

@router.post("/create-nail/")
async def create_nail(nail: NailBase, db: Session = Depends(get_db),token:str = Depends(oauth2_scheme)):
    nail_service = NailService(db)
    return nail_service.create_nail(nail,token=token)
@router.get("/get-nails")
async def get_nails(page: int = Query(1, ge=1),page_size: int = Query(10, ge=1, le=100),db: Session = Depends(get_db)):
    nail_service = NailService(db)
    return nail_service.get_nails(page=page, page_size=page_size)

