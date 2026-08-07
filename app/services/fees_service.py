# Placeholder for fees service
from sqlalchemy.orm import Session

from app.crud import fees as fees_crud
from app.schemas import fees as schemas


def create_fee(db: Session, fee_in: schemas.FeeCreate) -> schemas.Fee:
    return fees_crud.create_fee(db, fee_in)


def list_fees(db: Session, skip: int = 0, limit: int = 100):
    return fees_crud.get_fees(db, skip=skip, limit=limit)


def list_fees_by_student(db: Session, student_id: int, skip: int = 0, limit: int = 100):
    return fees_crud.get_fees_by_student(db, student_id=student_id, skip=skip, limit=limit)


def get_fee(db: Session, fee_id: int):
    return fees_crud.get_fee(db, fee_id=fee_id)


def update_fee(db: Session, fee_id: int, fee_update: schemas.FeeUpdate):
    return fees_crud.update_fee(db, fee_id=fee_id, fee_update=fee_update)


def delete_fee(db: Session, fee_id: int) -> bool:
    return fees_crud.delete_fee(db, fee_id=fee_id)

