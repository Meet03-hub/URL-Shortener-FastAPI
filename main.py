from fastapi import FastAPI

from database import engine
from database import Base
from models.user import User
from models.url import URL

from routers.auth import router as auth_router
from routers.url import router as url_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth_router)
app.include_router(url_router)

@app.get("/")
def home():
    return {
        "message": "URL Shortener API Running"
    }