"""
1. Employee and ProductionWorker Classes
Write an Employee class that keeps data attributes for the following pieces of information:
• Employee name
• Employee number
Next, write a class named ProductionWorker that is a subclass of the Employee class.
The ProductionWorker class should keep data attributes for the following information:
• Shift number (an integer, such as 1, 2, or 3)
• Hourly pay rate
The workday is divided into two shifts: day and night. The shift attribute will hold an
integer value representing the shift that the employee works. The day shift is shift 1 and the
night shift is shift 2. Write the appropriate accessor and mutator methods for each class.
Once you have written the classes, write a program that creates an object of the
ProductionWorker class and prompts the user to enter data for each of the object’s data
attributes. Store the data in the object, then use the object’s accessor methods to retrieve it
and display it on the screen.


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


class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self.__shift_number = shift_number
        self.__hourly_pay_rate = hourly_pay_rate

    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate


def main():
    name = input("enter employee name: ")
    number = input("enter employee number: ")
    shift_number = int(input("enter employee shift number: "))
    hourly_pay_rate = float(input("enter employee hourly pay rate: "))

    worker = ProductionWorker(name, number, shift_number, hourly_pay_rate)

    print(
        f"Employee name: {worker.get_name()}, Employee Number: {worker.get_number()}, Shift Number: {worker.get_shift_number()}, Hourly Pay Rate: {worker.get_hourly_pay_rate()}")


main()
