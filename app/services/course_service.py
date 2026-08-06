from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from crud import course as course_crud
from models.course import Course
from schemas.course import CourseCreate, CourseUpdate


def list_courses(
    db: Session,
    skip: int = 0,
    limit: int = 100
) -> list[Course]:
    return course_crud.get_all_courses(
        db=db,
        skip=skip,
        limit=limit
    )


def get_course(
    db: Session,
    course_id: int
) -> Course:
    course = course_crud.get_course_by_id(db, course_id)

    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found"
        )

    return course


def add_course(
    db: Session,
    course_data: CourseCreate
) -> Course:
    existing_code = course_crud.get_course_by_code(
        db,
        course_data.course_code
    )

    if existing_code:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Course code already exists"
        )

    existing_name = course_crud.get_course_by_name(
        db,
        course_data.course_name
    )

    if existing_name:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Course name already exists"
        )

    try:
        return course_crud.create_course(db, course_data)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Course already exists"
        )


def edit_course(
    db: Session,
    course_id: int,
    course_data: CourseUpdate
) -> Course:
    course = get_course(db, course_id)

    if course_data.course_code is not None:
        existing_code = course_crud.get_course_by_code(
            db,
            course_data.course_code
        )

        if existing_code and existing_code.id != course_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Course code already exists"
            )

    if course_data.course_name is not None:
        existing_name = course_crud.get_course_by_name(
            db,
            course_data.course_name
        )

        if existing_name and existing_name.id != course_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Course name already exists"
            )

    try:
        return course_crud.update_course(
            db,
            course,
            course_data
        )

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Course details already exist"
        )


def remove_course(
    db: Session,
    course_id: int
) -> None:
    course = get_course(db, course_id)
    course_crud.delete_course(db, course)
    
