# Placeholder for Teacher model
from sqlalchemy import Column, Integer, String, Date, DECIMAL, Text, TIMESTAMP
from sqlalchemy.sql import func

from app.database import Base


class Teacher(Base):
    __tablename__ = "teachers"

    teacher_id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(50), nullable=False)

    last_name = Column(String(50), nullable=False)

    email = Column(String(100), unique=True, nullable=False)

    phone = Column(String(15))

    subject = Column(String(100))

    qualification = Column(String(100))

    experience = Column(Integer)

    salary = Column(DECIMAL(10,2))

    address = Column(Text)

    hire_date = Column(Date)

    created_at = Column(TIMESTAMP, server_default=func.now())
