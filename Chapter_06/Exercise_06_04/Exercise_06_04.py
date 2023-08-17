"""
4. High Score
Assume that a file named scores.txt exists on the computer’s disk. It contains a series of
records, each with two fields – a name, followed by a score (an integer between 1 and 100).
Write a program that displays the name and score of the record with the highest score, as
well as the number of records in the file. (Hint: Use a variable and an “if” statement to
keep track of the highest score found as you read through the records, and a variable to
keep count of the number of records.)


@author Sharaf Qeshta
"""


def main():
    try:
        file = open("scores.txt")
        number_of_records = 0
        highest_score = 0
        for line in file:
            number_of_records += 1
            current_score = float(line.split(' ')[1])
            if current_score > highest_score:
                highest_score = current_score
        print(f"number of records in the file is : {number_of_records}")
        print(f"highest score is {highest_score}")
    except Exception as error:
        print(error)


main()
