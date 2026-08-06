from sqlalchemy import select
from sqlalchemy.orm import Session

from models.course import Course
from schemas.course import CourseCreate, CourseUpdate


def get_course_by_id(
    db: Session,
    course_id: int
) -> Course | None:
    statement = select(Course).where(Course.id == course_id)
    return db.scalar(statement)


def get_course_by_code(
    db: Session,
    course_code: str
) -> Course | None:
    statement = select(Course).where(
        Course.course_code == course_code
    )
    return db.scalar(statement)


def get_course_by_name(
    db: Session,
    course_name: str
) -> Course | None:
    statement = select(Course).where(
        Course.course_name == course_name
    )
    return db.scalar(statement)


def get_all_courses(
    db: Session,
    skip: int = 0,
    limit: int = 100
) -> list[Course]:
    statement = (
        select(Course)
        .order_by(Course.id)
        .offset(skip)
        .limit(limit)
    )

    return list(db.scalars(statement).all())


def create_course(
    db: Session,
    course_data: CourseCreate
) -> Course:
    new_course = Course(**course_data.model_dump())

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return new_course


def update_course(
    db: Session,
    course: Course,
    course_data: CourseUpdate
) -> Course:
    update_values = course_data.model_dump(exclude_unset=True)

    for field, value in update_values.items():
        setattr(course, field, value)

    db.commit()
    db.refresh(course)

    return course


def delete_course(
    db: Session,
    course: Course
) -> None:
    db.delete(course)
    db.commit()
    
