from Student import Student
from Course import Course
from Teacher import Teacher
from Required_Tables import *
from Admin import Admin
from Base import Session, engine, Base
from datetime import datetime

Base.metadata.create_all(engine)

session=Session()

def Dashboard():

    tempTeacher=Teacher("temp",1232,"phd",3,123)

    while True:

        menu_arr=[1,2,3,4]

        print("*********Course Management System***********")
        print("\n1. Login as Admin")
        print("2. Login as Student")
        print("3. Login as Teacher")
        print("4. Exit")
        print("\n")

        choice=0

        while True:
            try:
                choice=int(input("Please enter your choice: "))
                temp=menu_arr[choice-1]
                break
            except ValueError as ex:
                print("Enter an integer value (1-4)")
            except IndexError as ex:
                print("Enter from given choices (1-4)")

        if (choice == 1):
            Admin.AdminLogin()

        elif (choice == 2):
            Student.StudentLogin()

        elif (choice == 3):
            tempTeacher.TeacherLogin()

        elif (choice == 4):
            print("Exited Successfuly")
            break

Dashboard()



