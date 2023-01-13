from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from database import SessionLocal, engine

import json

import models
from schema import *

app = FastAPI()
app.title = "Courses Fast CURD"

models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


courses = json.loads(open("courses.json").read())["courses"]


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

