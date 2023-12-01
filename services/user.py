from sqlalchemy.orm import Session
from models import User
from schemas.user import UserBase
import bcrypt

class UserService:
    def __init__(self, db: Session):
        
        self.db = db
    def create_user(self, user: UserBase):
        hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())

        # Store the hashed password in the User model
        db_user = User(
            last_name=user.last_name,
            first_name=user.first_name,
            email=user.email,
            password=hashed_password.decode('utf-8')
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    def authenticate_user(self, email: str, password: str):
        user = self.db.query(User).filter(User.email == email).first()
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return True
        else:
            return False
