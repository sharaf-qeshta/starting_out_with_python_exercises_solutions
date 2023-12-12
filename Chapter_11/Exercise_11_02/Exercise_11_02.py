"""
Programming Exercises 597
2. ShiftSupervisor Class
In a particular factory, a shift supervisor is a salaried employee who supervises a shift. In
addition to a salary, the shift supervisor earns a yearly bonus when his or her shift meets
production goals. Write a ShiftSupervisor class that is a subclass of the Employee class
you created in Programming Exercise 1. The ShiftSupervisor class should keep a data
attribute for the annual salary, and a data attribute for the annual production bonus that
a shift supervisor has earned. Demonstrate the class by writing a program that uses a
ShiftSupervisor object.


@author Sharaf Qeshta
"""


class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number


class ShiftSupervisor(Employee):
    def __init__(self, name, number, annual_salary, bonus):
        super().__init__(name, number)
        self.__annual_salary = annual_salary
        self.__bonus = bonus

    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def get_bonus(self):
        return self.__bonus


def main():
    name = input("enter supervisor name: ")
    number = input("enter supervisor number: ")
    annual_salary = float(input("enter supervisor annual salary: "))
    bonus = float(input("enter supervisor bonus: "))

    supervisor = ShiftSupervisor(name, number, annual_salary, bonus)

    print(
        f"Supervisor name: {supervisor.get_name()}, Supervisor Number: {supervisor.get_number()}, Supervisor Annual "
        f"Salary: {supervisor.get_annual_salary()}, Bonus: {supervisor.get_bonus()}")


main()
