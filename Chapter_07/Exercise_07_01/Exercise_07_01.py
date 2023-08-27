"""
1. Valid Number Information
Design a program that uses a loop to build a list named valid_numbers that contains only
the numbers between 0 and 100 from the numbers list below. The program should then
determine and display the total and average of the values in the valid_numbers list.
numbers = [74, 19, 105, 20, −2, 67, 77, 124, −45, 38]


@author Sharaf Qeshta
"""


def main():
    numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]
    valid_numbers = []
    total = 0
    for i in range(101):
        if i in numbers:
            total += i
            valid_numbers.append(i)

    print(f"total numbers in valid_numbers list: {total}")
    print(f"the average number is: {total / len(valid_numbers)}")


main()
