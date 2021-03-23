from mymodules import *
import os

def course_data():
    print("Enter [C] to create a course")
    print("Enter [R] to show course list")
    print("Enter [D] to delete a course")
    print("Enter [Q] to quit")
    print("")

    user_option = input(str("Option : ")).upper()
    if user_option == "C":
        session_list = []
        course_name = input("New course name:").upper()
        while True:
            try:
                os.makedirs(course_name)
            except FileExistsError:
                print("Course file existed")
                print("Please enter another course code")
                course_name = input("\nNew course name:").upper()
            else:
                break
        print("\nThank You!\n")
        print(f"The course {course_name} has been added to the system\n")
        input("Press Enter to continue")
        os.system('cls')


    elif user_option == "R":
        course_list = os.listdir("attendance folder")
        print('{:<5} | {:<15}'.format("No.", "Course"))
        for count, line in enumerate(course_list, start=1):
                print('{:<5} | {:<15}|'.format(count,line))

        print("")
        input("Press Enter to continue")
        os.system('cls')

    elif user_option == "U":
        print("Change password")
        print('{:<5} | {:<15}| {:<15}| {:<15} '.format("No.", "Student name", "Student id", "Student login password"))
        for count, line in enumerate(student_list, start=1):
            print('{:<5} | {:<15}| {:<15}| {:<15} '.format(count, *line))
        print("")
        name = input("Please Enter the student name that you want to update...").upper()
        std_valid = find_element(name, student_list)
        while std_valid is None:
            print("Student not found")
            name = input("Please enter again!:")
            std_valid = find_element(name, student_list)

        print(f"\nStudent {name} is found")
        old_pwd = input("Please enter the old password for the student:")
        new_pwd = input("Please enter the new password for the student:")
        while old_pwd != student_list[std_valid][2]:
            print("Old password entered is wrong")
            old_pwd = input("Please enter again!:")
        student_list[std_valid][2] = new_pwd
        with open('student.txt', 'w') as file:
            for item in student_list:
                file.write("|".join(map(str, item)))
        print(f"\nStudent {name} 's login password has successfully updated.")
        input("\nPress Enter to continue")
        os.system('cls')

    elif user_option == "D":
        course_list = os.listdir("attendance folder")
        print('{:<5} | {:<15}'.format("No.", "Course"))
        for count, line in enumerate(course_list, start=1):
                print('{:<5} | {:<15}|'.format(count,line))
        print("")
        course_name = input("Please Enter the course that you want to delete...").upper()
        while True:
            try:
                os.remove(course_name)
            except:
                print("Course does not exist")
                course_name = input("Please Enter the course again!:").upper()
            else:
                break
        input("\nPress Enter to continue")
        os.system('cls')

    else:
        print("Invalid option.")
        os.system('cls')


