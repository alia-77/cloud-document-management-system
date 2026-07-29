from fastapi import FastAPI
from sqlalchemy import text

from app.api import users
from app.db.database import engine
from app.api.auth import router as auth_router
from app.api.documents import router as documents_router


app = FastAPI(
    title="Cloud Document Management System",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(users.router)
app.include_router(documents_router)

@app.get("/")
def root():
    return {
        "message": "Cloud Document Management System API"
    }

