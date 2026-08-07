from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    Enum,
    Text,
    DateTime,
    ForeignKey,
    func,
)

from app.database import Base



class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        unique=True,
        nullable=True
    )

    student_name = Column(String(100), nullable=False)

    gender = Column(
        Enum("Male", "Female", "Other"),
        nullable=True
    )

    date_of_birth = Column(Date, nullable=True)

    standard = Column(String(20), nullable=True)

    section = Column(String(10), nullable=True)

    roll_number = Column(
        String(20),
        unique=True,
        nullable=True
    )

    phone = Column(String(15), nullable=True)

    email = Column(String(100), nullable=True)

    address = Column(Text, nullable=True)

    admission_date = Column(Date, nullable=True)

    created_at = Column(
        DateTime,
        server_default=func.current_timestamp()
    )
