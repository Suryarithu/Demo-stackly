from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field

class AttendanceBase(BaseModel):
    student_id: int = Field(
        gt=0,
        examples=[1]
    )

    course_id: int = Field(
        gt=0,
        examples=[1]
    )

    attendance_date: date = Field(
        examples=["2026-08-07"]
    )

    status: str = Field(
        examples=["Present"]
    )

class AttendanceCreate(AttendanceBase):
    pass

class AttendanceResponse(AttendanceBase):
    id: int
    created_at: datetime | None = None
    model_config = ConfigDict(
        from_attributes=True
    )





