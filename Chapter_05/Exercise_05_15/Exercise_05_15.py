"""
15. Test Average and Grade
Write a program that asks the user to enter five test scores. The program should display a
letter grade for each score and the average test score. Write the following functions in the
program:
•	 calc_average. This function should accept five test scores as arguments and return the
average of the scores.
•	 determine_grade. This function should accept a test score as an argument and return
a letter grade for the score based on the following grading scale:


@author Sharaf Qeshta
"""


def calc_average(num1, num2, num3, num4, num5):
    return (num1 + num2 + num3 + num4 + num5) / 5


def determine_grade(grade):
    if grade >= 90:
        return "A"
    if grade >= 80:
        return "B"
    if grade >= 70:
        return "C"
    if grade >= 60:
        return "D"
    return "F"


grade1 = int(input("enter grade 1:"))
grade2 = int(input("enter grade 2:"))
grade3 = int(input("enter grade 3:"))
grade4 = int(input("enter grade 4:"))
grade5 = int(input("enter grade 5:"))

print(f"grade 1 is {determine_grade(grade1)}")
print(f"grade 2 is {determine_grade(grade2)}")
print(f"grade 3 is {determine_grade(grade3)}")
print(f"grade 4 is {determine_grade(grade4)}")
print(f"grade 5 is {determine_grade(grade5)}")
print(f"the average score is {calc_average(grade1, grade2, grade3, grade4, grade5)}")
