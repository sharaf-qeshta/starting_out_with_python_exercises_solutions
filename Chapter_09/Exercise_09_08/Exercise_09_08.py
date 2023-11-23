"""
8. Pickled Vegetables
Write a program that keeps vegetable names and prices in a dictionary as key-value pairs.
The program should display a menu that lets the user see a list of all vegetables and their
prices, add a new vegetable and price, change the price of an existing vegetable, and delete
an existing vegetable and price. The program should pickle the dictionary and save it to a
file when the user exits the program. Each time the program starts, it should retrieve the
dictionary from the file and unpickle it.

@author Sharaf Qeshta
"""

data = {}


def load_data():
    try:
        file = open("data.txt")
        for line in file:
            name_price = line.split(":")
            data[name_price[0]] = float(name_price[1])
        file.close()
    except Exception as error:
        print(error)


def load_data_back():
    try:
        file = open("data.txt", "w")
        for key, value in data.items():
            file.write(key + ":" + str(value) + "\n")
        file.close()
    except Exception as error:
        print(error)


def show_items_with_prices():
    for key, value in data.items():
        print(f"{key} : ${value}")


def add_item(item_name, item_price):
    if item_name in data:
        print(f"{item_name} is already exist.")
    else:
        data[item_name] = item_price


def update_item(item_name, item_price):
    if item_name in data:
        data[item_name] = item_price
        print("data updated successfully.")
    else:
        print(f"{item_name} is not exist.")


def delete_item(item_name):
    try:
        del data[item_name]
        print(f"{item_name} deleted successfully.")
    except KeyError:
        print(f"{item_name} is not in the list of items.")


def show_list():
    print("------------- main menu ------------------")
    print("1-view all items.")
    print("2-add an item.")
    print("3-update an item")
    print("4-delete an item")
    print("5-exit")


def view_all_items():
    print("------------- showing all items ------------------")
    show_items_with_prices()
    input("enter any key to go back.")
    show_main_menu()


def add_an_item():
    print("------------- adding an item ------------------")
    item_name = input("enter item name: ")
    item_price = float(input("enter item price: "))
    add_item(item_name, item_price)
    show_main_menu()


def update_an_item():
    print("------------- updating an item ------------------")
    item_name = input("enter item name: ")
    item_price = float(input("enter item price: "))
    update_item(item_name, item_price)
    show_main_menu()


def delete_an_item():
    print("------------- deleting an item ------------------")
    item_name = input("enter item name: ")
    delete_item(item_name)
    show_main_menu()


def show_main_menu():
    show_list()
    choice = input("enter a choice: ")
    if choice == '1':
        view_all_items()
    elif choice == '2':
        add_an_item()
    elif choice == '3':
        update_an_item()
    elif choice == '4':
        delete_an_item()
    else:
        load_data_back()


def main():
    load_data()
    show_main_menu()


main()
