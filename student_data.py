from mymodules import *
import os


def student_data():
    print("""
Enter [C] to create a student
Enter [R] to show student list
Enter [U] to change student login password
Enter [D] to delete a student
Enter [Q] to quit
""")

    student_list = []
    callTXTintoNestedList("student.txt", student_list)

    user_option = input(str("Option : ")).upper()
    if user_option == "C":
        name = input("Student name:").upper()
        while find_element(name,student_list) != None:
            print("Student already existed!")
            name = input("Please submit another student:").upper()
        std_id = str(int(student_list[-1][1]) + 1)
        pwd = "admin123"
        data = ("\n%s|%s|%s|" % (name, std_id, pwd))
        with open("student.txt", "r+") as f:
            f.read().rstrip('\n')#to avoid blank line while adding new student
            f.write(data)
        print("\nThank You!\n")
        print("The student has been added to the system")
        print(f"Name : {name}")
        print(f"Student id  : {std_id}")
        print(f"Default password : admin123")
        input("Press Enter to continue")
        os.system('cls')


    elif user_option == "R":
        print('{:<5} | {:<15}| {:<15}| {:<15} '.format("No.", "Student name", "Student id", "Student login password"))
        for count, line in enumerate(student_list, start=1):
            print('{:<5} | {:<15}| {:<15}| {:<15} '.format(count, *line))
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
        print('{:<5} | {:<15}| {:<15}| {:<15} '.format("No.", "Student name", "Student id", "Student login password"))
        for count, line in enumerate(student_list, start=1):
            print('{:<5} | {:<15}| {:<15}| {:<15} '.format(count, *line))
        print("")
        name = input("Please Enter the student name that you want to delete...").upper()
        std_valid = find_element(name, student_list)
        while name != "Q":
            while std_valid is None:
                print("Student not found")
                name = input("Please enter again!:")
                std_valid = find_element(name, student_list)
            print(f"\nStudent {name} is found")
            delete_a_line("student.txt", name)
            print(f"Student {name} has been deleted from system.")

        input("\nPress Enter to continue")
        os.system('cls')

    elif user_option == "Q":
        pass

    else:
        print("Invalid option.")
        os.system('cls')

student_data()
