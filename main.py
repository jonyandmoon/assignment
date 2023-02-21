from fastapi import FastAPI
from db import DB

app = FastAPI()


@app.get("/")
async def root():
    db=DB()
    return {db}