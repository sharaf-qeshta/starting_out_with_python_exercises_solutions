"""
7. Driver’s License Exam
The local driver’s license office has asked you to create an application that grades the
 written portion of the driver’s license exam. The exam has 20 multiple-choice questions. Here
are the correct answers:

Your program should store these correct answers in a list. The program should read the
student’s answers for each of the 20 questions from a text file and store the answers in
another list. (Create your own text file to test the application.) After the student’s answers
have been read from the file, the program should display a message indicating whether the
student passed or failed the exam. (A student must correctly answer 15 of the 20 questions
to pass the exam.) It should then display the total number of correctly answered questions,
the total number of incorrectly answered questions, and a list showing the question numbers
 of the incorrectly answered questions.


@author Sharaf Qeshta
"""

correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C',
                   'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']

def main():
    student_answers = []
    try:
        file = open("student_answers.txt")
        for line in file:
            student_answers.append(line.strip())
        wrong_count = 0
        for i in range(20):
            if correct_answers[i] != student_answers[i]:
                wrong_count += 1
        if wrong_count > 5:
            print("Student Failed with mark", 20-wrong_count, "out of 20")
        else:
            print("Student Pass with mark", 20 - wrong_count, "out of 20")
    except Exception as error:
        print(error)

main()