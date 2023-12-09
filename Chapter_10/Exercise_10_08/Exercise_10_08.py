"""
8. Cash Register
This exercise assumes you have created the RetailItem class for Programming Exercise 5.
 Create a CashRegister class that can be used with the RetailItem class. The
CashRegister class should be able to internally keep a list of RetailItem objects. The
class should have the following methods:
• A method named purchase_item that accepts a RetailItem object as an argument.
Each time the purchase_item method is called, the RetailItem object that is passed
as an argument should be added to the list.
• A method named get_total that returns the total price of all the RetailItem objects
stored in the CashRegister object’s internal list.
• A method named show_items that displays data about the RetailItem objects stored
in the CashRegister object’s internal list.
• A method named clear that should clear the CashRegister object’s internal list.
Demonstrate the CashRegister class in a program that allows the user to select several
items for purchase. When the user is ready to check out, the program should display a list
of all the items he or she has selected for purchase, as well as the total price.


@author Sharaf Qeshta
"""


class RetailItem:
    def __init__(self, description, units, price):
        self.__description = description
        self.__units = units
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_units(self, units):
        self.__units = units

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price


class CashRegister:
    def __init__(self):
        self.purchased_items = []

    def purchase_item(self, item):
        self.purchased_items.append(item)

    def get_total(self):
        total = 0
        for item in self.purchased_items:
            total += item.get_price() * item.get_units()
        return total

    def show_items(self):
        for item in self.purchased_items:
            print(f"description: {item.get_description()}, units: {item.get_units()}, price: ${item.get_price()}")

    def clear(self):
        self.purchased_items.clear()


def main():
    cash_register = CashRegister()
    while True:
        description = input("enter a description for the item: ")
        units = int(input("enter the units of the item: "))
        price = float(input("enter the price of the item: "))
        checkout = input("enter 0 for checkout: ")

        item = RetailItem(description, units, price)
        cash_register.purchase_item(item)

        if checkout == '0':
            break

    cash_register.show_items()
    print(f"total: ${cash_register.get_total()}")


main()

