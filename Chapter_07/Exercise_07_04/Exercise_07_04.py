"""
4. Number Analysis Program
Design a program that asks the user to enter a series of 20 numbers. The program should
store the numbers in a list then display the following data:
•	 The lowest number in the list
•	 The highest number in the list
•	 The total of the numbers in the list
•	 The average of the numbers in the list


@author Sharaf Qeshta
"""


def main():
    numbers = []
    numbers[0] = int(input("enter a number: "))
    total = 0
    lowest = numbers[0]
    highest = numbers[0]
    for i in range(19):
        number = int(input("enter a number: "))
        numbers[i] = number
        total += number
        if number < lowest:
            lowest = number
        if number > highest:
            highest = number
    print("The lowest number in the list is", lowest)
    print("The highest number in the list is", highest)
    print("The total of the numbers in the list is", total)
    print("The average of the numbers in the list is", total / 20)


main()
