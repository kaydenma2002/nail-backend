from fastapi import Depends, FastAPI
import models
from db import engine, Base
from routers import user,nail  # Import your user router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)

app.include_router(user.router)
app.include_router(nail.router)
    
