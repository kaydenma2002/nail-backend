from pydantic import BaseModel
class UserBase(BaseModel):
    last_name: str
    first_name: str
    email: str
    password: str

class NailBase(BaseModel):
    title: str
    content: str
    user_id: int