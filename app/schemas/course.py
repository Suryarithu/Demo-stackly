from pydantic import BaseModel, ConfigDict, Field


class CourseBase(BaseModel):
    course_name: str = Field(
        min_length=2,
        max_length=100,
        examples=["Bachelor of Computer Applications"]
    )

    course_code: str = Field(
        min_length=2,
        max_length=20,
        examples=["BCA101"]
    )

    department: str = Field(
        min_length=2,
        max_length=100,
        examples=["Computer Science"]
    )

    credits: int = Field(
        ge=1,
        le=10,
        examples=[4]
    )

    description: str | None = Field(
        default=None,
        max_length=500,
        examples=["Introduction to computer applications"]
    )


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    course_name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    course_code: str | None = Field(
        default=None,
        min_length=2,
        max_length=20
    )

    department: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    credits: int | None = Field(
        default=None,
        ge=1,
        le=10
    )

    description: str | None = Field(
        default=None,
        max_length=500
    )


class CourseResponse(CourseBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
