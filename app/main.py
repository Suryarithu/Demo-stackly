from fastapi import FastAPI

from models.course import Course
from routers.courses import router as course_router
from app.routers import auth
from app.routers import attendance
from .database import engine
from .routers import fees as fees_router
from .models import fees as fees_model

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



app = FastAPI(title="School Management Fees API", version="1.0")

app.include_router(fees_router.router, prefix="/fees", tags=["Fees"])


@app.on_event("startup")
def on_startup() -> None:
    fees_model.Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root() -> dict:
    return {"message": "School Management Fees API is running."}
