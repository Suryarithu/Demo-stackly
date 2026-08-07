from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class StudentBase(BaseModel):
    user_id: Optional[int] = None
    student_name: str
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    standard: Optional[str] = None
    section: Optional[str] = None
    roll_number: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    admission_date: Optional[date] = None


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    student_name: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[date] = None
    standard: Optional[str] = None
    section: Optional[str] = None
    roll_number: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None
    admission_date: Optional[date] = None


class StudentResponse(StudentBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
