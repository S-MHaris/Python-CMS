import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql
import sqlalchemy
import pymysql

engine = create_engine('mysql+pymysql://root:12345678@localhost/course_management', echo =False)

Session = sessionmaker(bind=engine)


Base = declarative_base()