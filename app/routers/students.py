# Placeholder for student routes
from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.student import (
    StudentCreate,
    StudentUpdate,
    StudentResponse,
)
from app.services import student_service

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.post(
    "/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return student_service.create_student(db, student)


@router.get(
    "/",
    response_model=List[StudentResponse]
)
def get_students(db: Session = Depends(get_db)):
    return student_service.get_all_students(db)


@router.get(
    "/{student_id}",
    response_model=StudentResponse
)
def get_student(student_id: int, db: Session = Depends(get_db)):
    return student_service.get_student(db, student_id)


@router.put(
    "/{student_id}",
    response_model=StudentResponse
)
def update_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):
    return student_service.update_student(db, student_id, student)


@router.delete(
    "/{student_id}",
    status_code=status.HTTP_200_OK
)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    return student_service.delete_student(db, student_id)
