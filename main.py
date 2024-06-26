from fastapi import FastAPI
from app.handlers import router

app = FastAPI()

app.include_router(router)
