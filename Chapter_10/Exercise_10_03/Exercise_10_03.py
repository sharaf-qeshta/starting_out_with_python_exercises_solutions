"""
3. Personal Information Class
Design a class that holds the following personal data: name, address, age, and phone number.
 Write appropriate accessor and mutator methods. Also, write a program that creates
three instances of the class. One instance should hold your information, and the other two
should hold your friends’ or family members’ information.

@author Sharaf Qeshta
"""


class Person:
    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    def set_name(self, name):
        self.__name = name

    def set_address(self, adress):
        self.__address = adress

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number


def main():
    person1 = Person("Sharaf Qeshta", "Houston, Texas", 22, "+99 456 852 4777")
    person2 = Person("John Smith", "London, UK", 25, "+99 456 852 4777")
    person3 = Person("Adam Adam", "Gaza, Palestine", 26, "+99 456 852 4777")
