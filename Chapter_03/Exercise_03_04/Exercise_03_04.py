"""
4. Roman Numerals
Write a program that prompts the user to enter a number within the range of 1 through 10.
The program should display the Roman numeral version of that number. If the number is
outside the range of 1 through 10, the program should display an error message.
The following table shows the Roman numerals for the numbers 1 through 10:

@author Sharaf Qeshta
"""


number = int(input("enter a number: "))

if number < 1:
    print("error")
elif number < 4:
    print("I" * number)
elif number == 4:
    print("IV")
elif number < 9:
    print("V", "I" * (number - 5), sep='')
elif number == 9:
    print("IX")
elif number == 10:
    print("X")
else:
    print("error")