"""
12. Average Steps Taken
A Personal Fitness Tracker is a wearable device that tracks your physical activity, calories
burned, heart rate, sleeping patterns, and so on. One common physical activity that most
of these devices track is the number of steps you take each day.
If you have downloaded this book’s source code from the Premium Companion Website,
you will find a file named steps.txt in the Chapter 06 folder. (The Premium Companion
Website can be found at www.pearsonglobaleditions.com/gaddis.) The steps.txt file
contains the number of steps a person has taken each day for a year. There are 365 lines
in the file, and each line contains the number of steps taken during a day. (The first line is
the number of steps taken on January 1st, the second line is the number of steps taken on
January 2nd, and so forth.) Write a program that reads the file, then displays the average
number of steps taken for each month. (The data is from a year that was not a leap year,
so February has 28 days.)


@author Sharaf Qeshta
"""


def main():
    try:
        file = open("steps.txt")

        total_steps = 0
        for i in range(31):  # january
            total_steps += int(file.readline())
        print("The average steps in January is", total_steps / 31, "a day")

        total_steps = 0
        for i in range(28):  # February
            total_steps += int(file.readline())
        print("The average steps in February is", total_steps / 28, "a day")

        total_steps = 0
        for i in range(31):  # March
            total_steps += int(file.readline())
        print("The average steps in March is", total_steps / 31, "a day")

        total_steps = 0
        for i in range(30):  # April
            total_steps += int(file.readline())
        print("The average steps in April is", total_steps / 30, "a day")

        total_steps = 0
        for i in range(31):  # May
            total_steps += int(file.readline())
        print("The average steps in May is", total_steps / 31, "a day")

        total_steps = 0
        for i in range(30):  # June
            total_steps += int(file.readline())
        print("The average steps in June is", total_steps / 30, "a day")

        total_steps = 0
        for i in range(31):  # July
            total_steps += int(file.readline())
        print("The average steps in July is", total_steps / 31, "a day")

        total_steps = 0
        for i in range(31):  # August
            total_steps += int(file.readline())
        print("The average steps in August is", total_steps / 31, "a day")

        total_steps = 0
        for i in range(30):  # September
            total_steps += int(file.readline())
        print("The average steps in September is", total_steps / 30, "a day")

        total_steps = 0
        for i in range(31):  # October
            total_steps += int(file.readline())
        print("The average steps in October is", total_steps / 31, "a day")

        total_steps = 0
        for i in range(30):  # November
            total_steps += int(file.readline())
        print("The average steps in November is", total_steps / 30, "a day")

        total_steps = 0
        for i in range(31):  # December
            total_steps += int(file.readline())
        print("The average steps in December is", total_steps / 31, "a day")

    except Exception as error:
        print(error)


main()
