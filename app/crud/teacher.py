# Placeholder for teacher CRUD operations
from sqlalchemy.orm import Session

from app.models.teacher import Teacher
from app.schemas.teacher import TeacherCreate, TeacherUpdate


def get_teacher_by_email(db: Session, email: str):
    return db.query(Teacher).filter(
        Teacher.email == email
    ).first()


def create_teacher(db: Session, teacher: TeacherCreate):
    new_teacher = Teacher(**teacher.model_dump())

    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)

    return new_teacher


def get_all_teachers(db: Session):
    return db.query(Teacher).all()


def get_teacher_by_id(db: Session, teacher_id: int):
    return db.query(Teacher).filter(
        Teacher.teacher_id == teacher_id
    ).first()


def update_teacher(
    db: Session,
    teacher: Teacher,
    teacher_data: TeacherUpdate
):
    for key, value in teacher_data.model_dump().items():
        setattr(teacher, key, value)

    db.commit()
    db.refresh(teacher)

    return teacher


def delete_teacher(
    db: Session,
    teacher: Teacher
):
    db.delete(teacher)
    db.commit()

    return True
