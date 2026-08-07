# Placeholder for teacher routes
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.teacher import (
    TeacherCreate,
    TeacherUpdate,
    TeacherResponse
)
from app.services import teacher_service

router = APIRouter(
    prefix="/teachers",
    tags=["Teachers"]
)


@router.post("/", response_model=TeacherResponse)
def add_teacher(
    teacher: TeacherCreate,
    db: Session = Depends(get_db)
):
    return teacher_service.create_teacher(db, teacher)


@router.get("/", response_model=list[TeacherResponse])
def get_teachers(db: Session = Depends(get_db)):
    return teacher_service.get_all_teachers(db)


@router.get("/{teacher_id}", response_model=TeacherResponse)
def get_teacher(
    teacher_id: int,
    db: Session = Depends(get_db)
):
    return teacher_service.get_teacher_by_id(db, teacher_id)


@router.put("/{teacher_id}", response_model=TeacherResponse)
def update_teacher(
    teacher_id: int,
    teacher: TeacherUpdate,
    db: Session = Depends(get_db)
):
    return teacher_service.update_teacher(
        db,
        teacher_id,
        teacher
    )


@router.delete("/{teacher_id}")
def delete_teacher(
    teacher_id: int,
    db: Session = Depends(get_db)
):
    return teacher_service.delete_teacher(db, teacher_id)
