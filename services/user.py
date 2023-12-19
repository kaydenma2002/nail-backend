from sqlalchemy.orm import Session
from models import User
from schemas.user import UserBase, LoginData
from typing import Annotated
from datetime import datetime, timedelta
from typing import Union, Any
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import httpx

from fastapi import Depends, FastAPI, HTTPException, status
import bcrypt
from jose import JWTError, jwt
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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
    def create_access_token(data: dict, expires_delta: timedelta | None = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    def authenticate_user(self, login_data: LoginData):
        user = self.db.query(User).filter(User.email == login_data.email).first()
        if user and bcrypt.checkpw(login_data.password.encode('utf-8'), user.password.encode('utf-8')):
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = self.create_access_token(data={"sub": login_data.email}, expires_delta=access_token_expires)
            user = {
            "id": user.id,
            "last_name": user.last_name,
            "first_name": user.first_name,
            "email": user.email,
            "address": user.address,
        }
            return  {"access_token": access_token, "token_type": "bearer","user":user}
        else:
            raise HTTPException(status_code=400, detail="username or password not match. Please try again.")
    def get_user_from_token(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception

        user = self.db.query(User).filter(User.email == email).first()
        if user is None:
            raise credentials_exception

        return user
    
    async def connect_to_dropbox(self, access_token: str, file_path: str):
        # Make Dropbox API requests using the provided access token
        headers = {"Authorization": f"Bearer {access_token}"}
        
        # Check if the file exists
        # file_exists = await self.check_dropbox_file_existence(access_token, file_path)
        # if not file_exists:
        #     raise HTTPException(status_code=404, detail=f"File not found at path: {file_path}")

        # Continue with connecting to Dropbox and other operations if needed

        async with httpx.AsyncClient() as client:
            # Example Dropbox API request to get user account information
            response = await client.post("https://api.dropboxapi.com/2/file_requests/list_v2", headers=headers)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Dropbox API request failed")

        user_info = response.json()

        # Example: Now, let's download the file after successfully connecting
        # file_content = await self.download_dropbox_file(access_token, file_path)

        return {"message": "Connected to Dropbox", "user_info": user_info}

    async def check_dropbox_file_existence(self, access_token: str, file_path: str):
        headers = {"Authorization": f"Bearer {access_token}"}
        params = {"path": file_path}

        async with httpx.AsyncClient() as client:
            response = await client.post("https://api.dropboxapi.com/2/files/get_metadata", headers=headers, params=params)

        return response.status_code == 200

    async def download_dropbox_file(self, access_token: str, file_path: str):
        # Make Dropbox API requests to download the file
        headers = {"Authorization": f"Bearer {access_token}"}
        params = {"path": file_path}

        async with httpx.AsyncClient() as client:
            response = await client.post("https://content.dropboxapi.com/2/files/download", headers=headers, params=params)

        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Dropbox API request failed")

        file_content = response.content
        return file_content
    

    

    
    
    
