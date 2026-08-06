Database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:stackly%4012345@localhost/school_management"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
main.py
from fastapi import FastAPI

from app.database import Base, engine
from app.routers import teacher
from app.models import teacher as teacher_model

Base.metadata.create_all(bind=engine)

app = FastAPI(title="School Management System")

app.include_router(teacher.router)

@app.get("/")
def home():
    return {"message": "School Management System API"}

models
teacher.py
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
routers
teacher.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.teacher import Teacher
from app.schemas.teacher import TeacherCreate, TeacherUpdate, TeacherResponse

router = APIRouter(
    prefix="/teachers",
    tags=["Teachers"]
)

# Add Teacher
@router.post("/", response_model=TeacherResponse)
def add_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    existing = db.query(Teacher).filter(
        Teacher.email == teacher.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_teacher = Teacher(**teacher.model_dump())

    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)

    return new_teacher

# View All Teachers
@router.get("/", response_model=list[TeacherResponse])
def get_teachers(db: Session = Depends(get_db)):
    return db.query(Teacher).all()

# View Teacher by ID
@router.get("/{teacher_id}", response_model=TeacherResponse)
def get_teacher(teacher_id: int, db: Session = Depends(get_db)):
    teacher = db.query(Teacher).filter(
        Teacher.teacher_id == teacher_id
    ).first()

    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    return teacher

# Update Teacher
@router.put("/{teacher_id}", response_model=TeacherResponse)
def update_teacher(
    teacher_id: int,
    updated: TeacherUpdate,
    db: Session = Depends(get_db)
):
    teacher = db.query(Teacher).filter(
        Teacher.teacher_id == teacher_id
    ).first()

    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    
    if teacher.email != updated.email:
        existing = db.query(Teacher).filter(
            Teacher.email == updated.email
        ).first()

        if existing:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

    for key, value in updated.model_dump().items():
        setattr(teacher, key, value)

    db.commit()
    db.refresh(teacher)

    return teacher

# Delete Teacher
@router.delete("/{teacher_id}")
def delete_teacher(
    teacher_id: int,
    db: Session = Depends(get_db)
):
    teacher = db.query(Teacher).filter(
        Teacher.teacher_id == teacher_id
    ).first()

    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="Teacher not found"
        )

    db.delete(teacher)
    db.commit()

    return {"message": "Teacher deleted successfully"}
schemas
teacher.py
from pydantic import BaseModel, EmailStr
from datetime import date

class TeacherCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    subject: str
    qualification: str
    experience: int
    salary: float
    address: str
    hire_date: date

class TeacherUpdate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    subject: str
    qualification: str
    experience: int
    salary: float
    address: str
    hire_date: date

class TeacherResponse(TeacherCreate):
    teacher_id: int

    class Config:
        from_attributes = True

