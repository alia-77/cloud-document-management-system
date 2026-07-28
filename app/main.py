from fastapi import FastAPI

app = FastAPI(
    title="Cloud Document Management System",
    version="1.0.0",
    description="A cloud-native document management system built with FastAPI."
)


@app.get("/")
def root():
    return {
        "message": "Cloud Document Management System API"
    }