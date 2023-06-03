"""
7. Grade Calculator
A class has two tests worth 25 points each along with a main exam worth 50 points. For a student
to pass the class, they must obtain an overall score of at least 50 points, and must obtain at
least 25 points in the main exam. If a student’s total score is less than 50 or they obtain less than
25 points in the main exam, they receive a grade of “Fail”. Otherwise, their grade is as follows:
If they get more than 80, they get a grade of “Distinction”. 50–59 = “Pass”.
If they get less than 80 but more than 60, they get a “Credit” grade.
If they get less than 60, they get a ”Pass” grade.
Write a program that prompts the user to enter their points for both tests and the exam and
converts the values to integers. The program should first check if the points entered for the
tests and exam are valid. If any of the test scores are not between 0 and 25, or the exam
score is not between 0 and 50, the program should display an error message. Otherwise,
the program should display the total points and the grade.


@author Sharaf Qeshta
"""

test1_score = int(input("enter the first test grade:"))
test2_score = int(input("enter the second test grade:"))
main_exam_score = int(input("enter the main exam grade:"))

if test1_score < 0 or test1_score > 25 or test2_score < 0 or test2_score > 25 or main_exam_score < 0 or main_exam_score > 50:
    print("error")
else:
    overall_score = test2_score + test1_score + main_exam_score
    if overall_score >= 80:
        print("Distinction")
    elif overall_score >= 60:
        print("Credit")
    else:
        print("Pass")
