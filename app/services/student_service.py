from sqlalchemy.orm import Session

from app.crud.student import (
    create_student,
    get_all_students,
    get_student_by_id,
    update_student,
    delete_student,
)
from app.schemas.student import StudentCreate, StudentUpdate


def create_student_service(db: Session, student: StudentCreate):
    return create_student(db, student)


def get_all_students_service(db: Session):
    return get_all_students(db)


def get_student_by_id_service(db: Session, student_id: int):
    return get_student_by_id(db, student_id)


def update_student_service(db: Session, student_id: int, student: StudentUpdate):
    return update_student(db, student_id, student)


def delete_student_service(db: Session, student_id: int):
    return delete_student(db, student_id)
