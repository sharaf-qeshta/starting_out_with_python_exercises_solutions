"""
1. Name Display
Write a program that gets strings containing a person’s first and last name as separate
values, and then displays their “initials”, “name in address book”, and “username”. For
example, if the user enters a first name of “John” and a last name of “Smith”, the program
should display “J.S.”, “John SMITH”, and “jsmith”.

@author Sharaf Qeshta
"""


def main():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    print(f"Initials: {first_name.upper()[0]}.{last_name.upper()[0]}.")
    print(f"Name in Address book: {first_name} {last_name}")
    print(f"username:{first_name.lower()[0]}{last_name.lower()}")


main()
