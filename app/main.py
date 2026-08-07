from fastapi import FastAPI

from models.course import Course
from routers.courses import router as course_router
from app.routers import auth
from app.routers import attendance

app = FastAPI(
    title="School Management System API",
    version="1.0.0"
)

app.include_router(auth.router)
app.include_router(course_router)
app.include_router(attendance.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to School Management System API"
    }
