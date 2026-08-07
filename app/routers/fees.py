# Placeholder for fees routes
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas import fees as schemas
from app.services import fees_service


class FeeStatusUpdate(BaseModel):
    status: schemas.PaymentStatus


router = APIRouter()


@router.post("/", response_model=schemas.Fee, status_code=status.HTTP_201_CREATED)
def create_fee(fee_in: schemas.FeeCreate, db: Session = Depends(get_db)):
    return fees_service.create_fee(db, fee_in)


@router.get("/", response_model=list[schemas.Fee])
def list_fees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return fees_service.list_fees(db, skip=skip, limit=limit)


@router.get("/student/{student_id}", response_model=list[schemas.Fee])
def list_fees_by_student(student_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return fees_service.list_fees_by_student(db, student_id=student_id, skip=skip, limit=limit)


@router.get("/{fee_id}", response_model=schemas.Fee)
def get_fee(fee_id: int, db: Session = Depends(get_db)):
    fee = fees_service.get_fee(db, fee_id=fee_id)
    if not fee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fee record not found")
    return fee


@router.patch("/{fee_id}", response_model=schemas.Fee)
def update_fee(fee_id: int, fee_update: schemas.FeeUpdate, db: Session = Depends(get_db)):
    fee = fees_service.update_fee(db, fee_id=fee_id, fee_update=fee_update)
    if not fee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fee record not found")
    return fee


@router.patch("/{fee_id}/status", response_model=schemas.Fee)
def update_payment_status(fee_id: int, status_update: FeeStatusUpdate, db: Session = Depends(get_db)):
    fee_update = schemas.FeeUpdate(status=status_update.status)
    fee = fees_service.update_fee(db, fee_id=fee_id, fee_update=fee_update)
    if not fee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fee record not found")
    return fee


@router.delete("/{fee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_fee(fee_id: int, db: Session = Depends(get_db)):
    success = fees_service.delete_fee(db, fee_id=fee_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Fee record not found")
    return None
