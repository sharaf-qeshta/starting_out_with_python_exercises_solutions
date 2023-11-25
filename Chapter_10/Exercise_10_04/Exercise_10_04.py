"""
4. Employee Class
Write a class named Employee that holds the following data about an employee in attributes:
 name, ID number, department, and job title.
Once you have written the class, write a program that creates three Employee objects to
hold the following data:
Name ID Number Department Job Title
Susan Meyers 47899 Accounting Vice President
Mark Jones 39119 IT Programmer
Joy Rogers 81774 Manufacturing Engineer
The program should store this data in the three objects, then display the data for each
employee on the screen.


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


def main():
    employee1 = Employee("Susan Meyers", "478990",
                         "Accounting", "Vice President")
    employee2 = Employee("Mark Jones", "39119",
                         "IT", "Programmer")
    employee3 = Employee("Joy Rogers", "81774",
                         "Manufacturing", "Engineer")

    print(
        f"name: {employee1.get_name()}, id: {employee1.get_id_number()}, Department: {employee1.get_department()}, Job Title: {employee1.get_job_title()}")
    print(
        f"name: {employee2.get_name()}, id: {employee2.get_id_number()}, Department: {employee2.get_department()}, Job Title: {employee2.get_job_title()}")
    print(
        f"name: {employee3.get_name()}, id: {employee3.get_id_number()}, Department: {employee3.get_department()}, Job Title: {employee3.get_job_title()}")


main()
