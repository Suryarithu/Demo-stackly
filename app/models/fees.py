# Placeholder for Fees model
import enum

from sqlalchemy import Column, Date, DateTime, Enum, Float, Integer, String, Text
from sqlalchemy.sql import func

from app.database import Base


class PaymentStatus(str, enum.Enum):
    pending = "pending"
    partial = "partial"
    paid = "paid"


class Fee(Base):
    __tablename__ = "fees"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, nullable=False, index=True)
    student_name = Column(String(100), nullable=True)
    amount = Column(Float, nullable=False)
    paid_amount = Column(Float, nullable=False, default=0.0)
    status = Column(Enum(PaymentStatus), nullable=False, default=PaymentStatus.pending)
    due_date = Column(Date, nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

