from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.nail import NailService
from db import get_db
from schemas.nail import NailBase

router = APIRouter()

@router.post("/create-nail/")
async def create_nail(nail: NailBase, db: Session = Depends(get_db)):
    nail_service = NailService(db)
    return nail_service.create_nail(nail)


