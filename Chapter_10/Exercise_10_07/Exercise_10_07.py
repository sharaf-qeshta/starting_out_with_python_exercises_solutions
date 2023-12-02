"""
7. Employee Management System
This exercise assumes you have created the Employee class for Programming Exercise 4.
Create a program that stores Employee objects in a dictionary. Use the employee ID number
as the key. The program should present a menu that lets the user perform the following
actions:
• Look up an employee in the dictionary
• Add a new employee to the dictionary
• Change an existing employee’s name, department, and job title in the dictionary
• Delete an employee from the dictionary
• Quit the program
When the program ends, it should pickle the dictionary and save it to a file. Each time the
program starts, it should try to load the pickled dictionary from the file. If the file does not
exist, the program should start with an empty dictionary.

@author Sharaf Qeshta
"""


class Employee:
    def __init__(self, name, id_number,
                 department, job_title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def set_department(self, department):
        self.__department = department

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_department(self):
        return self.__department

    def get_job_title(self):
        return self.__job_title


data = {}


def download_data():
    try:
        file = open("data.txt")
        for line in file:
            line = line.replace("\n", "")
            object_data = line.split(";")
            employee = Employee(object_data[0].strip(), object_data[1].strip(),
                                object_data[2].strip(), object_data[3].strip())
            data[employee.get_id_number()] = employee
        file.close()
    except Exception as error:
        print(error)


def upload_data():
    try:
        file = open("data.txt", "w")
        for key, value in data.items():
            file.write(value.get_name() + ";" + value.get_id_number() + ";"
                       + value.get_department() + ";" + value.get_job_title() + "\n")
        file.close()
    except Exception as error:
        print(error)


def look_up():
    print("-------------- look up an employee ---------------")
    emp_id = input("enter employee id: ")
    emp_name = input("enter employee name: ")
    emp_department = input("enter employee department: ")
    emp_job_title = input("enter employee job title: ")

    for key, value in data.items():
        if value.get_name == emp_name or value.get_id_number == emp_id \
                or value.get_department == emp_department or value.get_job_title == emp_job_title:
            print_employee(value)
    main_menu()


def add_new_employee():
    print("-------------- add new employee ---------------")
    emp_id = input("enter employee id: ")
    emp_name = input("enter employee name: ")
    emp_department = input("enter employee department: ")
    emp_job_title = input("enter employee job title: ")

    if emp_id in data.keys():
        print(f"Employee with id {emp_id} exist in the system!")
    else:
        data[emp_id] = Employee(emp_name, emp_id, emp_department, emp_job_title)
        print("Employee Added Successfully")
    main_menu()


def update_an_employee():
    print("-------------- add new employee ---------------")
    emp_id = input("enter employee id: ")
    emp_name = input("enter employee name: ")
    emp_department = input("enter employee department: ")
    emp_job_title = input("enter employee job title: ")

    if emp_id in data.keys():
        data[emp_id] = Employee(emp_id, emp_name, emp_department, emp_job_title)
        print("Employee updated successfully")
    else:
        print(f"Employee with id {emp_id} is not exist in the system!")
    main_menu()


def delete_an_employee():
    print("-------------- delete an employee ---------------")
    emp_id = input("enter employee id: ")

    try:
        del data[emp_id]
        print(f"{emp_id} deleted successfully.")
    except:
        print(f"employee with id {emp_id} is not exist in the system!")
    main_menu()


def print_employee(employee):
    print(f"name: {employee.get_name()}, id: "
          f"{employee.get_id_number()}, department: {employee.get_department()},"
          f" job title: {employee.get_job_title()}")


def print_menu():
    print("1-Look up an employee")
    print("2-Add a new employee")
    print("3-Update an employee")
    print("4-Delete an employee")
    print("5-Quit")


def main_menu():
    print_menu()
    choice = int(input("enter a choice: "))
    if choice == 1:
        look_up()
    elif choice == 2:
        add_new_employee()
    elif choice == 3:
        update_an_employee()
    elif choice == 4:
        delete_an_employee()


def main():
    download_data()
    main_menu()
    upload_data()


main()
