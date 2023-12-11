from pydantic import BaseModel


class UserBase(BaseModel):
    last_name: str | None = None
    first_name: str | None = None
    email: str
    password: str
    
class LoginData(BaseModel):
    email: str
    password: str


