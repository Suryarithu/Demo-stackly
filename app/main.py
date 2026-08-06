from fastapi import FastAPI

from app.routers import auth

app = FastAPI(
    title="School Management System API",
    version="1.0.0"
)

app.include_router(auth.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to School Management System API"
    }