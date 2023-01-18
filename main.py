from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal, engine

# import json

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


@app.post("/courses/")
def create_course(course: Course):
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

@app.get("/courses/{course_id}")
def read_course(course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.put("/courses/{course_id}")
def update_course(course_id: int, course: Course):
    db_course = db.query(Course).filter(Course.id == course_id).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    db_course.name = course.name
    db_course.teacher_id = course.teacher_id
    db_course.time_slot = course.time_slot
    db_course.capacity = course.capacity
    db.commit()
    return db_course

@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(course)
    db.commit()
    return {"message": "Course deleted"}

@app.get("/courses/")
def read_courses(skip: int = 0, limit: int = 100):
    courses = db.query(Course).offset(skip).limit(limit).all()
    return courses

@app.post("/teachers/")
def create_teacher(teacher: Teacher):
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher
