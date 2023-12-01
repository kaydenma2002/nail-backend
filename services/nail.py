from sqlalchemy.orm import Session
from models import Nail
from schemas.nail import NailBase

class NailService:
    def __init__(self, db: Session):
        
        self.db = db
    def create_nail(self, nail: NailBase):
        

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
    
