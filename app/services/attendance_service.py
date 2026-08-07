from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from crud import attendance as attendance_crud
from models.attendance import Attendance
from schemas.attendance import AttendanceCreate

def list_attendance(
    db: Session,
    skip: int = 0,
    limit: int = 100
) -> list[Attendance]:

    return attendance_crud.get_all_attendance(
        db=db,
        skip=skip,
        limit=limit
    )


def get_attendance(
    db: Session,
    attendance_id: int
) -> Attendance:

    attendance = attendance_crud.get_attendance_by_id(
        db,
        attendance_id
    )

    if attendance is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attendance record not found"
        )

    return attendance


def list_student_attendance(
    db: Session,
    student_id: int,
    skip: int = 0,
    limit: int = 100
) -> list[Attendance]:

    return attendance_crud.get_attendance_by_student(
        db=db,
        student_id=student_id,
        skip=skip,
        limit=limit
    )


def mark_attendance(
    db: Session,
    attendance_data: AttendanceCreate
) -> Attendance:

    if attendance_data.status not in [
        "Present",
        "Absent",
        "Leave"
    ]:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Status must be Present, Absent, or Leave"
        )

    return attendance_crud.create_attendance(
        db,
        attendance_data
    )
