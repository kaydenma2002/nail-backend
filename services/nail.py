from sqlalchemy.orm import Session
from sqlalchemy import func

from models import Nail
from models import User
from schemas.nail import NailBase
from fastapi import Query
from services.user import UserService
class NailService:
    def __init__(self, db: Session):
        self.user_service = UserService(db)
        self.db = db
    def create_nail(self, nail: NailBase,token:str):
        user = self.user_service.get_user_from_token(token)

        # Store the hashed password in the Nail model
        db_nail = Nail(
            title=nail.title,
            content=nail.content,
            address=nail.address
        )
        self.db.add(db_nail)
        self.db.commit()
        self.db.refresh(db_nail)
        return db_nail
    def get_nails(self, page: int = Query(1, ge=1), page_size: int = Query(10, ge=1, le=100)):
        # user = self.user_service.get_user_from_token(token)
        
        try:
           
            # Calculate the offset based on page number and page size
            offset = (page - 1) * page_size

            # Use paginate to retrieve a specific page of results
            query = self.db.query(Nail).offset(offset).limit(page_size)
            nails = query.all()
            total_count = self.db.query(func.count(Nail.id)).scalar()

            return {"nails": nails, "total_count": total_count}
        except Exception as e:
            
            return None
    
