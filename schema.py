from pydantic import BaseModel
from typing import Union

class Student(BaseModel):
    id: int
    name: str
    email: str
    rollno: str
    major: str

    class Config: #takes ORM objects and translate them into responses automatically
        orm_mode = True


class CourseDetail(BaseModel):
    id: int
    name: str
    description: str
    credits: int

    class Config:
        orm_mode = True


class Course(BaseModel):
    id: int
    code: str
    course_detail: Union[CourseDetail, None] = None
    students: Union[Student, None] = None

    class Config:
        orm_mode = True
