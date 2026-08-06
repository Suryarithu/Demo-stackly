from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.orm import Session

from database import get_db
from schemas.course import (
    CourseCreate,
    CourseResponse,
    CourseUpdate
)
from services import course_service


router = APIRouter(
    prefix="/courses",
    tags=["Courses"]
)


@router.post(
    "",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED
)
def create_course(
    course_data: CourseCreate,
    db: Session = Depends(get_db)
):
    return course_service.add_course(db, course_data)


@router.get(
    "",
    response_model=list[CourseResponse]
)
def get_courses(
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return course_service.list_courses(
        db=db,
        skip=skip,
        limit=limit
    )


@router.get(
    "/{course_id}",
    response_model=CourseResponse
)
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    return course_service.get_course(db, course_id)


@router.put(
    "/{course_id}",
    response_model=CourseResponse
)
def update_course(
    course_id: int,
    course_data: CourseUpdate,
    db: Session = Depends(get_db)
):
    return course_service.edit_course(
        db,
        course_id,
        course_data
    )


@router.delete(
    "/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):
    course_service.remove_course(db, course_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

