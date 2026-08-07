from sqlalchemy import select
from sqlalchemy.orm import Session
from models.attendance import Attendance
from schemas.attendance import AttendanceCreate

def get_attendance_by_id(
    db: Session,
    attendance_id: int
) -> Attendance | None:
    statement = select(Attendance).where(
        Attendance.id == attendance_id
    )

    return db.scalar(statement)

def get_all_attendance(
    db: Session,
    skip: int = 0,
    limit: int = 100
) -> list[Attendance]:

    statement = (
        select(Attendance)
        .order_by(Attendance.id)
        .offset(skip)
        .limit(limit)
    )

    return list(db.scalars(statement).all())

def get_attendance_by_student(
    db: Session,
    student_id: int,
    skip: int = 0,
    limit: int = 100
) -> list[Attendance]:

    statement = (
        select(Attendance)
        .where(Attendance.student_id == student_id)
        .order_by(Attendance.attendance_date.desc())
        .offset(skip)
        .limit(limit)
    )

    return list(db.scalars(statement).all())

def create_attendance(
    db: Session,
    attendance_data: AttendanceCreate
) -> Attendance:

    new_attendance = Attendance(
        **attendance_data.model_dump()
    )

    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)

    return new_attendance



