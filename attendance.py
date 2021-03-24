from mymodules import *
from course_data import *
import os


def attendance():
    print("""
1.Create new attendance file
2.Read or Update existing attendance file
3.Delete attendance file
""")
    user_option = input(str("Option : ")).upper()
    if user_option == "1":
        create_attn()
    elif user_option == "2":
        update_attn()
    elif user_option == "3":
        delete_attn()
    elif user_option == "Q":
        pass


def create_attn():
    student_list = []
    callTXTintoNestedList("student.txt", student_list)
    for std in student_list:
        std[2] = ""#clear the password in each std

    course_name = input("Enter course:").upper()
    course_exist = os.path.exists(os.path.join("attendance folder",course_name))
    while course_exist is not True:
            print("Course not existed")
            course_name = input("You may create the course by enter [C]\nor Enter course again:").upper()
            if course_name == "C":
                create_course()
            elif course_name == "Q":
                attendance()
                return
            course_exist = os.path.exists(os.path.join("attendance folder", course_name))
    session = input("Week:").upper()
    session_txt = session + ".txt"
    file_name = os.path.join("attendance folder",course_name,session_txt)
    session_exist = os.path.isfile(file_name)
    while session_exist is True:
        print("Attendance file existed")
        print("Please key in another session")
        print("Enter [U] to update the existing attendance file")
        session = input("Week:").upper()
        if session == "U":
            update_attn()
            return
        if session == "Q":
            attendance()
            return
        session_txt = "week" + session + ".txt"
        file_name = os.path.join("attendance folder", course_name, session_txt)
    session_start = input("Session starts by(HH:MM):")
    session_end = input("Session ends by(HH:MM):")
    print('{:<5} | {:<15}| {:<15}|{:<25}  '.format("No.", "Student name", "Student id", "Joined time(HH:MM) or just [P]resent/[A]bsent/[L]ate"))
    for count, line in enumerate(student_list, start=1):
        print('{:<5} | {:<15}| {:<15}| '.format(count, *line), end="")
        login_time = (input().strip()).upper()
        if login_time  in( "Present" ,"Absent" ,"Late"):
            line[2] = login_time
        else:
            while True:
                try:
                    line[2] = attendance_status(session_start, session_end, login_time)
                except:
                    print("Invalid input")
                    login_time = (input(f"Please reenter the attendance status for {line[0]}: ").strip()).upper()
                else:
                    break
    with open(file_name, "w") as file:
        for item in student_list:
            file.write("|".join(map(str, item)))
    print(session_txt ,"has been created")

def update_attn():
    course_name = input("Enter course:").upper()
    course_exist = os.path.exists(os.path.join("attendance folder",course_name))
    while course_exist is not True:
            print("Course not existed")
            course_name = input("You may create the course by enter [C]\nor Enter course again:").upper()
            if course_name == "C":
                create_course()
            course_exist = os.path.exists(os.path.join("attendance folder", course_name))
    session = input("Week:").upper()
    session_txt = session + ".txt"
    file_name = os.path.join("attendance folder",course_name,session_txt)
    attn_list = []
    while True:
        try:
            callTXTintoNestedList(file_name,attn_list)
        except:
            print("Attendance file does not exist")
            session = input("Week:").upper()
            file_name = os.path.join(course_name, "week" +session + ".txt")
            if session == "Q":
                attendance()
                return
        else:
            break
    quit = ""
    while quit != "Q":
        print('{:<5} | {:<15}| {:<15}|{:<25}  '.format("No.", "Student name", "Student id", "Attendance Status"))
        for count, line in enumerate(attn_list, start=1):
            print('{:<5} | {:<15}| {:<15}| {:<5} '.format(count, *line))
        std_name = input("Please enter the name of the student to update:").upper()
        std = find_element(std_name,attn_list)
        while std is None:
            print("Student not found")
            std_name = input("Please enter the name of the student to update:").upper()
            if std_name == "Q":
                attendance()
        attn_status = input("Please enter Present/Absent/Late:").upper()
        while attn_status not in ("Present" ,"Absent" , "Late"):
            print("Invalid input")
            attn_status = input("Please enter Present/Absent/Late")
        attn_list[std][2] = attn_status
        with open(file_name, 'w') as file:
            for item in attn_list:
                file.write("|".join(map(str, item)))
        print(f"\nStudent {std_name} 's attendance status has successfully updated.\n")
        input()
        os.system('cls')

        quit = input("\nPress Enter to update another student\nOr else, press [Q]uit.").upper()

def delete_attn():
    course_name = input("Enter course:").upper()
    course_exist = os.path.exists(os.path.join("attendance folder",course_name))
    while course_exist is not True:
            print("Course not existed")
            course_name = input("Enter course again:").upper()
            if course_name == "Q":
                attendance()
            course_exist = os.path.exists(os.path.join("attendance folder", course_name))
    session = input("Week:").upper()
    file_name = os.path.join(course_name, session + ".txt")
    while True:
        try:
            os.remove(file_name)
        except:
            session = input("Week:").upper()
            file_name = os.path.join(course_name, session + ".txt")
        else:
            break



