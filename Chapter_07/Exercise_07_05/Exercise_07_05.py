"""
5. Charge Account Validation
If you have downloaded the source code from the Premium Companion Website you will
find a file named charge_accounts.txt in the Chapter 07 folder. This file has a list of a
company’s valid charge account numbers. Each account number is a seven-digit number,
such as 5658845.
Write a program that reads the contents of the file into a list. The program should then
ask the user to enter a charge account number. The program should determine whether
the number is valid by searching for it in the list. If the number is in the list, the program
should display a message indicating the number is valid. If the number is not in the list, the
program should display a message indicating the number is invalid.
(You can access the Premium Companion Website at www.pearsonglobaleditions.com/gaddis.)


@author Sharaf Qeshta
"""


def main():
    charge_accounts = []
    try:
        file = open("charge_accounts.txt")
        for line in file:
            charge_accounts.append(line)
    except Exception as error:
        print(error)

    number_to_look_for = input("enter a charge account number: ")

    found = False
    for account in charge_accounts:
        if account == number_to_look_for:
            print(f"account number {number_to_look_for} exist in the file")
            found = True

    if not found:
        print(f"account number {number_to_look_for} is not exist in the file")


main()
