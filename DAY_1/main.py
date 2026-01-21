from fastapi import FastAPI
from routes import router

app = FastAPI(title = "FastAPI")

app.include_router(router)