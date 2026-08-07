# Placeholder for Fees schema
from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class PaymentStatus(str, Enum):
    pending = "pending"
    partial = "partial"
    paid = "paid"


class FeeBase(BaseModel):
    student_id: int
    student_name: Optional[str] = None
    amount: float
    paid_amount: Optional[float] = 0.0
    status: PaymentStatus = PaymentStatus.pending
    due_date: Optional[date] = None
    description: Optional[str] = None


class FeeCreate(FeeBase):
    pass


class FeeUpdate(BaseModel):
    student_name: Optional[str] = None
    amount: Optional[float] = None
    paid_amount: Optional[float] = None
    status: Optional[PaymentStatus] = None
    due_date: Optional[date] = None
    description: Optional[str] = None


class Fee(FeeBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

