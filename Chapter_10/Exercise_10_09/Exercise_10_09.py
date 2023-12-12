"""
9. Trivia Game
In this programming exercise, you will create a simple trivia game for two players. The pro-
gram will work like this:
• Starting with player 1, each player gets a turn at answering 5 trivia questions. (There
should be a total of 10 questions.) When a question is displayed, 4 possible answers are
also displayed. Only one of the answers is correct, and if the player selects the correct
answer, he or she earns a point.
• After answers have been selected for all the questions, the program displays the number
of points earned by each player and declares the player with the highest number of points
the winner.

To create this program, write a Question class to hold the data for a trivia question. The
Question class should have attributes for the following data:
• A trivia question
• Possible answer 1
• Possible answer 2
• Possible answer 3
• Possible answer 4
• The number of the correct answer (1, 2, 3, or 4)
The Question class also should have an appropriate _ _ init_ _ method, accessors, and
mutators.
The program should have a list or a dictionary containing 10 Question objects, one for
each trivia question. Make up your own trivia questions on the subject or subjects of your
choice for the objects.


@author Sharaf Qeshta
"""


class Question:
    def __init__(self, question, answer1, answer2, answer3
                 , answer4, correct_answer_number):
        self.__question = question
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__correct_answer_number = correct_answer_number

    def set_question(self, question):
        self.__question = question

    def set_answer1(self, answer1):
        self.__answer1 = answer1

    def set_answer2(self, answer2):
        self.__answer2 = answer2

    def set_answer3(self, answer3):
        self.__answer3 = answer3

    def set_answer4(self, answer4):
        self.__answer4 = answer4

    def set_correct_answer_number(self, correct_answer_number):
        self.__correct_answer_number = correct_answer_number

    def get_question(self):
        return self.__question

    def get_answer1(self):
        return self.__answer1

    def get_answer2(self):
        return self.__answer2

    def get_answer3(self):
        return self.__answer3

    def get_answer4(self):
        return self.__answer4

    def get_correct_answer_number(self):
        return self.__correct_answer_number


def main():
    questions = [Question("what is the capital of netherlands?", "Amsterdam",
                          "Berlin", "Broxel", "Paris", 1),
                 Question("in what year the american civil war ended?", 1863,
                          1861, 1912, 1865, 4),
                 Question("what happens if two objects moving at the speed of light collide?",
                          "black hole created", "Release of infinite energy",
                          "the two objects will disappear", "the two objects crashes", 2),
                 Question("Who painted the Mona Lisa?",
                          "Leonardo da Vinci", "Pablo Picasso",
                          "Vincent van Gogh", "Rembrandt", 1),
                 Question("who is the greatest scientist in the 20th century?",
                          "Albert Einstein", "Robert Oppenheimer",
                          "Nikola Tesla", "Marie Curie", 3),
                 ]

    player1_correct_answers = 0
    print("Player 1 Turn.")
    for question in questions:
        print(question.get_question())
        print(f"1.{question.get_answer1()}")
        print(f"2.{question.get_answer2()}")
        print(f"3.{question.get_answer3()}")
        print(f"4.{question.get_answer4()}")
        answer = int(input("enter you choice: "))
        if answer == question.get_correct_answer_number():
            player1_correct_answers += 1

    player2_correct_answers = 0
    print("Player 2 Turn.")
    for question in questions:
        print(question.get_question())
        print(f"1.{question.get_answer1()}")
        print(f"2.{question.get_answer2()}")
        print(f"3.{question.get_answer3()}")
        print(f"4.{question.get_answer4()}")
        answer = int(input("enter you choice: "))
        if answer == question.get_correct_answer_number():
            player2_correct_answers += 1

    print(f"Player 1 scores {player1_correct_answers} out of 5.")
    print(f"Player 2 scores {player2_correct_answers} out of 5.")


main()
