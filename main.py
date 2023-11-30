from fastapi import FastAPI
from config.db import connect,initialize_db

app = FastAPI()
conn = connect()
cursor = conn.cursor()
@app.on_event("startup")
async def startup_event():
    initialize_db()
