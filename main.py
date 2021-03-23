from student_data import *
from attendance import *
from mymodules import *
from student_entry import *
from report import *
from course_data import *
import os

def main():
    while 1:
        print("Welcome to the UTAR SMART Student Management & Attendance Registration Technology")
        print("")
        print("1. Login as student")
        print("2. Login as admin")

        user_option = input(str("Option : "))
        if user_option == "1":
            auth_student()
        elif user_option == "2":
            auth_admin()
        else:
            print("No valid option was selected")
            os.system('cls')
            

def auth_student():#login verification
    global id_no , pwd
    student_list = []
    print("")
    print("Student's Login")
    print("")
    id_no = input("Id_no:")
    pwd = input("Password:")
    callTXTintoNestedList("student.txt",student_list)
    std_valid = find_element(id_no,student_list)
    if std_valid != None and student_list[std_valid][2] == pwd:
        student_session()
    else:
        print("\nUser doesn't exist or wrong password!\n")
        os.system('cls')

def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "admin":
        if password == "password":
            admin_session()
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognised")
        os.system('cls')

def student_session():
    print("")
    print("1. View attendance")
    print("2. Change password")
    user_option = input(str("Option : "))
    if user_option == "1":
        view_attendance(id_no)
    elif user_option == "2":
        change_password(id_no,pwd)
    else:
        print("No valid option was selected")
        os.system('cls')


def admin_session():
    print("")
    print("1.CRUD Student data")
    print("2.CRUD course")
    print("3.CRUD Student Attendance")
    print("4.Generate Bar List")
    print("5.Generate 100% attendance report")
    user_option = input(str("Option : "))
    if user_option == "1":
        student_data()
    elif user_option == "2":
        course_data()
    elif user_option == "3":
        attendance()
    elif user_option == "4":
        barlist()
    elif user_option == "5":
        full_attendance()
    else:
        print("No valid option was selected")
        os.system('cls')


main()

