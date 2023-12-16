from pydantic import BaseModel


class ReservationBase(BaseModel):
    customer_id: int
    worker_id: int
    date: str
    status: int
    



