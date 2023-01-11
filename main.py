from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Student(BaseModel):
    id: int
    name: str
    email: str
    rollno: str
class CourseDetail(BaseModel):
    id:int
    description: str
    students: Union[Student, None] = None

class Course(BaseModel):
    id: int
    code: str
    name: str
    credits : int
    course_detail : Union[CourseDetail, None] = None


courses = [
    {
        "id": 1,
        "code": "CS101",
        "name": "Introduction to Computer Science",
        "credits": 3,
        "course_detail": {
            "id": 1,
            "description": "This course provides an introduction to the intellectual enterprises of computer science and the art of programming.",
            "students": [
                {
                    "id": 1,
                    "name": "Muhammad Waleed",
                    "email": "mwfarrukh@gmail.com",
                    "rollno":"20b-115-se"
                },
                {
                    "id": 2,
                    "name": "Farhan Ali",
                    "email": "farhanali@gmail.com",
                    "rollno":"20b-055-se"
                },
                {
                    "id": 3,
                    "name": "Bajwa",
                    "email": "bajwa@gmail.com",
                    "rollno":"20b-017-se"
                },
            ]
        }
    },
    {
        "id": 2,
        "code": "C222",
        "name": "Data Communication and Computer Networks",
        "credits": 3,
        "course_detail": {
            "id": 1,
            "description": "This course provides an introduction of computer networks.",
            "students": [
                {
                    "id": 1,
                    "name": "Muhammad Waleed",
                    "email": "mwfarrukh@gmail.com",
                    "rollno":"20b-115-se"
                },
                {
                    "id": 2,
                    "name": "Farhan Ali",
                    "email": "farhanali@gmail.com",
                    "rollno":"20b-055-se"
                },
                {
                    "id": 3,
                    "name": "Bajwa",
                    "email": "bajwa@gmail.com",
                    "rollno":"20b-017-se"
                },
            ]
        }
    }
]


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/courses")
async def get_courses():
    return courses

@app.get("/courses/{course_id}")
async def get_course(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return course
    return {"error": "Course not found"}

@app.get("/courses/{course_id}/students")
async def get_students(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return course["course_detail"]["students"]
    return {"error": "Course not found"}

@app.get("/students")
async def get_students():
    students = []
    for course in courses:
        students.extend(course["course_detail"]["students"])
    return students

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    for course in courses:
        for student in course["course_detail"]["students"]:
            if student["id"] == student_id:
                return student
    return {"error": "Student not found"}