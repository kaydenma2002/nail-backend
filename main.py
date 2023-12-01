from fastapi import Depends, FastAPI
import models
from db import engine, Base
from routers import user,nail  # Import your user router


app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(nail.router)
    
