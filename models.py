from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
from database import Base

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String)
    course_detail = relationship("CourseDetail", back_populates="course")
    student = relationship("Student", back_populates="course")


class CourseDetail(Base):
    __tablename__ = "course_details"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    credits = Column(Integer)
    course = relationship("Course", back_populates="course_detail")

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    rollno = Column(String)
    major = Column(String)
    course = relationship("Course", back_populates="student")
