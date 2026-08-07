# Placeholder for fees CRUD operations
from typing import List, Optional

from sqlalchemy.orm import Session

from app.models import fees as models
from app.schemas import fees as schemas


def get_fee(db: Session, fee_id: int) -> Optional[models.Fee]:
    return db.query(models.Fee).filter(models.Fee.id == fee_id).first()


def get_fees(db: Session, skip: int = 0, limit: int = 100) -> List[models.Fee]:
    return db.query(models.Fee).offset(skip).limit(limit).all()


def get_fees_by_student(db: Session, student_id: int, skip: int = 0, limit: int = 100) -> List[models.Fee]:
    return (
        db.query(models.Fee)
        .filter(models.Fee.student_id == student_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


def create_fee(db: Session, fee: schemas.FeeCreate) -> models.Fee:
    db_fee = models.Fee(**fee.dict())
    db.add(db_fee)
    db.commit()
    db.refresh(db_fee)
    return db_fee


def update_fee(db: Session, fee_id: int, fee_update: schemas.FeeUpdate) -> Optional[models.Fee]:
    db_fee = get_fee(db, fee_id)
    if not db_fee:
        return None
    update_data = fee_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_fee, key, value)

    if "paid_amount" in update_data or "amount" in update_data:
        if db_fee.paid_amount >= db_fee.amount:
            db_fee.status = models.PaymentStatus.paid
        elif db_fee.paid_amount > 0:
            db_fee.status = models.PaymentStatus.partial
        else:
            db_fee.status = models.PaymentStatus.pending

    db.commit()
    db.refresh(db_fee)
    return db_fee


def delete_fee(db: Session, fee_id: int) -> bool:
    db_fee = get_fee(db, fee_id)
    if not db_fee:
        return False
    db.delete(db_fee)
    db.commit()
    return True

