"""
3. Person and Customer Classes
Write a class named Person with data attributes for a person’s name, address, and telephone number.
 Next, write a class named Customer that is a subclass of the Person class.
The Customer class should have a data attribute for a customer number, and a Boolean
data attribute indicating whether the customer wishes to be on a mailing list. Demonstrate
an instance of the Customer class in a simple program.


@author Sharaf Qeshta
"""


class Person:
    def __init__(self, name, address, telephone_number):
        self.__name = name
        self.__address = address
        self.__telephone_number = telephone_number

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_telephone_number(self, telephone_number):
        self.__telephone_number = telephone_number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_telephone_number(self):
        return self.__telephone_number


class Customer(Person):
    def __init__(self, name, address, telephone_number,
                 customer_number, allowing_mailing):
        super().__init__(name, address, telephone_number)
        self.__customer_number = customer_number
        self.__allowing_mailing = allowing_mailing

    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    def set_allowing_mailing(self, allowing_mailing):
        self.__allowing_mailing = allowing_mailing

    def get_customer_number(self):
        return self.__customer_number

    def get_allowing_mailing(self):
        return self.__allowing_mailing


def main():
    customer = Customer("Sharaf", "Houston, TX", "123456789",
                        712, True)

    print(customer.get_name())
    print(customer.get_address())
    print(customer.get_telephone_number())
    print(customer.get_customer_number())
    print(customer.get_allowing_mailing())


main()
