from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from database import SessionLocal, engine

import json

import models
from models import *
from schema import *

app = FastAPI()
app.title = "Courses"

models.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# courses = json.loads(open("courses.json").read())["courses"]

db = SessionLocal()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/courses")
async def get_courses():
    return db.query(Course).all()


@app.get("/courses/{course_id}")
async def get_course(course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


@app.get("/courses/{course_id}/students")
async def get_students(course_id: int):
    return db.query(Student).filter(Student.course_id == course_id).all()


@app.get("/students")
async def get_students():
    return db.query(Student).all()


@app.get("/students/{student_id}")
async def get_student(student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()

@app.post("/courses")
async def create_course(c: course_schema):
    db_course = Course(code=c.code)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@app.post("/courses/course_details")
async def create_course_detail(c: courseDetail_schema):
    db_course_detail = CourseDetail(name=c.name, description=c.description, credits=c.credits)
    db.add(db_course_detail)
    db.commit()
    db.refresh(db_course_detail)
    return db_course_detail

