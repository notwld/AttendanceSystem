from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
from database import Base

from datetime import datetime
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    time_slot = Column(String)
    capacity = Column(Integer)
    students = relationship("Student", secondary="enrollments", back_populates="courses")
    teacher = relationship("Teacher", back_populates="courses")

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", back_populates="teacher")

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    courses = relationship("Course", secondary="enrollments", back_populates="students")
    attendances = relationship("Attendance", back_populates="student")

class Enrollment(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    student = relationship("Student", back_populates="courses")
    course = relationship("Course", back_populates="students")

class Attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    date = Column(datetime, default=datetime.utcnow)
    status = Column(String)
    student = relationship("Student", back_populates="attendances")
    course = relationship("Course", back_populates="attendances")

class Manager(Base):
    __tablename__ = 'managers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)