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


@app.get("/db-test")
def database_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

        return {
            "database": result.scalar()
        }