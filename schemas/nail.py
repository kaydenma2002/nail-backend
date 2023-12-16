from pydantic import BaseModel


class NailBase(BaseModel):
    title: str
    content: str
    user_id: int
    address: str
    