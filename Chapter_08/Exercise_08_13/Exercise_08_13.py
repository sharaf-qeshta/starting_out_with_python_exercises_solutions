"""
13. PowerBall Lottery
To play the PowerBall lottery, you buy a ticket that has five numbers in the range of 1–69,
and a “PowerBall” number in the range of 1–26. (You can pick the numbers yourself, or you
can let the ticket machine randomly pick them for you.) Then, on a specified date, a winning
set of numbers is randomly selected by a machine. If your first five numbers match the first
five winning numbers in any order, and your PowerBall number matches the winning PowerBall number,
 then you win the jackpot, which is a very large amount of money. If your
numbers match only some of the winning numbers, you win a lesser amount, depending on
how many of the winning numbers you have matched.
In the student sample programs for this book, you will find a file named pbnumbers.txt,
containing the winning PowerBall numbers that were selected between February 3, 2010
and May 11, 2016 (the file contains 654 sets of winning numbers). Figure 8-6 shows an
example of the first few lines of the file’s contents. Each line in the file contains the set of six
numbers that were selected on a given date. The numbers are separated by a space, and the
last number in each line is the PowerBall number for that day. For example, the first line in
the file shows the numbers for February 3, 2010, which were 17, 22, 36, 37, 52, and the
PowerBall number 24.

Write one or more programs that work with this file to perform the following:
• Display the 10 most common numbers, ordered by frequency
• Display the 10 least common numbers, ordered by frequency
• Display the 10 most overdue numbers (numbers that haven’t been drawn in a long
time), ordered from most overdue to least overdue
• Display the frequency of each number 1–69, and the frequency of each Powerball
number 1–26

@author Sharaf Qeshta
"""

FREQUENCY = {}
FREQUENCY_OF_POWERBALL = {}


def load_frequency():
    try:
        file = open("pbnumbers.txt")
        for line in file:
            numbers_in_line = line.split(" ")
            for i in range(5):
                int_number = int(numbers_in_line[i])
                if int_number in FREQUENCY.keys():
                    FREQUENCY[int_number] += 1
                else:
                    FREQUENCY[int_number] = 1
            # dealing with the powerball number
            int_number = int(numbers_in_line[5])
            if int_number in FREQUENCY_OF_POWERBALL.keys():
                FREQUENCY_OF_POWERBALL[int_number] += 1
            else:
                FREQUENCY_OF_POWERBALL[int_number] = 1
    except Exception as error:
        print(error)


def print_10_most_used(dictionary):
    # last 10 values
    for i in range(10):
        print(dictionary[i + 59], end=', ')
    print()


def print_10_least_used(dictionary):
    # first 10 values
    for i in range(10):
        print(dictionary[i + 1], end=', ')
    print()


def print_the_frequency():
    for i in FREQUENCY.keys():
        print(f"{i} : {FREQUENCY[i]}", end=', ')
    print()

    for i in FREQUENCY_OF_POWERBALL.keys():
        print(f"{i} : {FREQUENCY_OF_POWERBALL[i]}", end=', ')
    print()


def main():
    load_frequency()
    sorted_frequency = sorted(FREQUENCY.items(), key=lambda x: x[1])
    print_10_most_used(sorted_frequency)
    print_10_least_used(sorted_frequency)
    print_the_frequency()


main()
