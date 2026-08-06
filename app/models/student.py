# Placeholder for Student model
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.sql import func

from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(15), nullable=False)
    gender = Column(String(10), nullable=False)
    date_of_birth = Column(Date, nullable=False)
    address = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
