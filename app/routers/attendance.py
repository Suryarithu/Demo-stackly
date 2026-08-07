from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from database import get_db
from schemas.attendance import (
    AttendanceCreate,
    AttendanceResponse
)
from services import attendance_service

router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)

@router.post(
    "",
    response_model=AttendanceResponse,
    status_code=status.HTTP_201_CREATED
)
def mark_attendance(
    attendance_data: AttendanceCreate,
    db: Session = Depends(get_db)
):

    return attendance_service.mark_attendance(
        db,
        attendance_data
    )

@router.get(
    "",
    response_model=list[AttendanceResponse]
)
def get_attendance(
    skip: int = Query(
        default=0,
        ge=0
    ),
    limit: int = Query(
        default=100,
        ge=1,
        le=100
    ),
    db: Session = Depends(get_db)
):

    return attendance_service.list_attendance(
        db=db,
        skip=skip,
        limit=limit
    )

@router.get(
    "/{attendance_id}",
    response_model=AttendanceResponse
)
def get_attendance_by_id(
    attendance_id: int,
    db: Session = Depends(get_db)
):

    return attendance_service.get_attendance(
        db,
        attendance_id
    )

@router.get(
    "/student/{student_id}",
    response_model=list[AttendanceResponse]
)
def get_student_attendance(
    student_id: int,
    skip: int = Query(
        default=0,
        ge=0
    ),
    limit: int = Query(
        default=100,
        ge=1,
        le=100
    ),
    db: Session = Depends(get_db)
):
    return attendance_service.list_student_attendance(
        db=db,
        student_id=student_id,
        skip=skip,
        limit=limit
    )
