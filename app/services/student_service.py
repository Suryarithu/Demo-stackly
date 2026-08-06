# Placeholder for student service
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.crud import student as student_crud
from app.schemas.student import StudentCreate, StudentUpdate


def create_student(db: Session, student: StudentCreate):
    existing_student = student_crud.get_student_by_email(db, student.email)

    if existing_student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Student with this email already exists."
        )

    return student_crud.create_student(db, student)


def get_all_students(db: Session):
    return student_crud.get_students(db)


def get_student(db: Session, student_id: int):
    student = student_crud.get_student_by_id(db, student_id)

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found."
        )

    return student


def update_student(db: Session, student_id: int, student: StudentUpdate):
    existing_student = student_crud.get_student_by_id(db, student_id)

    if not existing_student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found."
        )

    if student.email:
        email_exists = student_crud.get_student_by_email(db, student.email)

        if email_exists and email_exists.id != student_id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists."
            )

    return student_crud.update_student(db, student_id, student)


def delete_student(db: Session, student_id: int):
    student = student_crud.get_student_by_id(db, student_id)

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found."
        )

    student_crud.delete_student(db, student_id)

    return {"message": "Student deleted successfully."}
