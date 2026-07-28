from fastapi import FastAPI
from sqlalchemy import text

from app.db.database import engine


app = FastAPI(
    title="Cloud Document Management System",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Cloud Document Management System API"
    }

