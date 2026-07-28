from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import engine
from app.api.auth import router as auth_router


app = FastAPI(
    title="Cloud Document Management System",
    version="1.0.0"
)

app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "message": "Cloud Document Management System API"
    }

