from sqlalchemy import Column, String, Integer, Table, Date, ForeignKey
from sqlalchemy.orm import relationship
from Base import Base
import datetime


class Course_Teacher_Association(Base):
    __tablename__ = 'Course_Teacher_Association'

    CR_TR_ID = Column(Integer, primary_key=True, autoincrement=True)
    CR_ID = Column(Integer, ForeignKey('Course.CR_ID'))
    TR_ID = Column(Integer, ForeignKey('Teacher.TR_ID'))

    course_relation = relationship('Course', backref='Course_Teacher_Association')
    teacher_relation = relationship('Teacher', backref='Course_Teacher_Association')

    def __init__(self,C_ID,T_ID):
        self.CR_ID=C_ID
        self.TR_ID=T_ID

class Course_Student_Association(Base):
    __tablename__ = 'Course_Student_Association'

    CR_ST_ID = Column(Integer, primary_key=True, autoincrement=True)
    CR_ID = Column(Integer, ForeignKey('Course.CR_ID'))
    ST_ID = Column(Integer, ForeignKey('Student.ST_ID'))

    course_relation = relationship('Course', backref='Course_Student_Association')
    student_relation = relationship('Student', backref='Course_Student_Association')

    def __init__(self,C_ID,S_ID):
        self.CR_ID=C_ID
        self.ST_ID=S_ID

class Assignment(Base):

    __tablename__ = 'Assignment'

    AS_ID = Column(Integer, primary_key=True, autoincrement=True)
    AS_Topic = Column(String(50))
    AS_Description = Column(String(150))
    AS_Deadline = Column(Date)

    def __init__(self,topic,desc,deadline):
        self.AS_Topic=topic
        self.AS_Description=desc
        self.AS_Deadline=deadline


class Teacher_Assignment_Association(Base):

    __tablename__ = 'Teacher_Assignment_Association'

    TR_AS_ID = Column(Integer,primary_key=True,autoincrement=True)
    TR_ID= Column(Integer, ForeignKey('Teacher.TR_ID'))
    AS_ID = Column(Integer, ForeignKey('Assignment.AS_ID'))

    teacher_relation = relationship('Teacher', backref='Teacher_Assignment_Association')
    assignment_relation = relationship('Assignment', backref='Teacher_Assignment_Association')

    def __init__(self,t_id,a_id):

        self.TR_ID=t_id
        self.AS_ID=a_id


class Attendance(Base):

    __tablename__ = 'Attendance'

    AT_ID = Column(Integer,primary_key=True,autoincrement=True)
    TR_ID = Column(Integer,ForeignKey('Teacher.TR_ID'))
    ST_ID = Column(Integer,ForeignKey('Student.ST_ID'))
    CR_ID = Column(Integer,ForeignKey('Course.CR_ID'))
    ST_Name = Column(String(50))
    AT_Date = Column(Date)
    AT_Status = Column(String(10))
    
    teacher_relation=relationship('Teacher', backref='Attendance')
    course_relation=relationship('Course', backref='Attendance')
    student_relation=relationship('Student', backref='Attendance')

    def __init__(self,t_id,s_id,c_id,name,date,status):

        self.TR_ID=t_id
        self.ST_ID=s_id
        self.CR_ID=c_id
        self.ST_Name=name
        self.AT_Date=date
        self.AT_Status=status

