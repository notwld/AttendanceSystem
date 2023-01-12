from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.title = "Courses Fast CURD"

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
    major: str


class CourseDetail(BaseModel):
    id: int
    name: str
    description: str
    credits: int


class Course(BaseModel):
    id: int
    code: str
    course_detail: Union[CourseDetail, None] = None
    students: Union[Student, None] = None


courses = [
    {
        "id": 1,
        "code": "CS101",
        "course_detail": {
            "id": 1,
            "name": "Introduction to Computer Science",
            "credits": 3,
            "description": "This course provides an introduction to the intellectual enterprises of computer science and the art of programming.",
        },
        "students": [
            {
                "id": 1,
                "name": "Muhammad Waleed",
                "email": "mwfarrukh@gmail.com",
                "rollno": "20b-115-se",
                "major":"Software Engineering"
            },
            {
                "id": 2,
                "name": "Farhan Ali",
                "email": "farhanali@gmail.com",
                "rollno": "20b-055-se",
                "major":"Software Engineering"
            },
            {
                "id": 3,
                "name": "Bajwa",
                "email": "bajwa@gmail.com",
                "rollno": "20b-017-se",
                "major":"Software Engineering"
            },
        ]
    },
    {
        "id": 2,
        "code": "C222",
        "course_detail": {
            "name": "Data Communication and Computer Networks",
            "credits": 3,
            "id": 1,
            "description": "This course provides an introduction of computer networks.",
        },
        "students": [
            {
                "id": 1,
                "name": "Muhammad Waleed",
                "email": "mwfarrukh@gmail.com",
                "rollno": "20b-115-se",
                "major":"Software Engineering"
            },
            {
                "id": 2,
                "name": "Farhan Ali",
                "email": "farhanali@gmail.com",
                "rollno": "20b-055-se",
                "major":"Software Engineering"
            },
            {
                "id": 3,
                "name": "Bajwa",
                "email": "bajwa@gmail.com",
                "rollno": "20b-017-se",
                "major":"Software Engineering"
            },
        ]
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
            return course["students"]
    return {"error": "Course not found"}


@app.get("/students")
async def get_students():
    students = []
    for course in courses:
        for student in course["students"]:
            if student not in students:
                students.append(student)
    return students


@app.get("/students/{student_id}")
async def get_student(student_id: int):
    for course in courses:
        for student in course["students"]:
            if student["id"] == student_id:
                return student
    return {"error": "Student not found"}

@app.post("/courses")
async def create_course(course: Course):
    courses.append(course.dict())
    return {
        "message": "Course created successfully",
    }

@app.post("/courses/{course_id}/students")
async def create_student(course_id: int, student: Student):
    student_id = student.id
    for course in courses:
        for student in course["students"]:
            if student["id"] == student_id:
                return {"error": "Student already exists"}
    for course in courses:
        if course["id"] == course_id:
            course["students"].append(student.dict())
            return {
                "message": "Student created successfully",
            }
    return {"error": "Course not found"}

@app.put("/courses/{course_id}")
async def update_course(course_id: int, course: Course):
    for index, course in enumerate(courses):
        if course["id"] == course_id:
            courses[index] = course.dict()
            return {
                "message": "Course updated successfully",
            }
    return {"error": "Course not found"}

@app.put("/courses/students/{student_id}")
async def update_student(student_id: int, student: Student):
    for course in courses:
        for index, student in enumerate(course["students"]):
            if student["id"] == student_id:
                course["students"][index] = student.dict()
                return {
                    "message": "Student updated successfully",
                }
    return {"error": "Student not found"}

@app.delete("/courses/{course_id}")
async def delete_course(course_id: int):
    for index, course in enumerate(courses):
        if course["id"] == course_id:
            courses.pop(index)
            return {
                "message": "Course deleted successfully",
            }
    return {"error": "Course not found"}

@app.delete("/courses/students/{student_id}")
async def delete_student(student_id: int):
    for course in courses:
        for index, student in enumerate(course["students"]):
            if student["id"] == student_id:
                course["students"].pop(index)
                return {
                    "message": "Student deleted successfully",
                }
    return {"error": "Student not found"}

