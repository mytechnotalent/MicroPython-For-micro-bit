from random import choice
from data import questions


class Question:
    """
    Class to implement micro:bit specific question for escape room
    """

    @staticmethod
    def get_random_question():
        """Method to get a random question from the database

        Returns:
            str, str, str, str, str, str
        """
        random_question = choice(list(questions))
        answer_1 = questions[random_question][0]
        answer_2 = questions[random_question][1]
        answer_3 = questions[random_question][2]
        correct_answer_index = questions[random_question][3]
        correct_answer = questions[random_question][correct_answer_index]
        return random_question, answer_1, answer_2, answer_3, correct_answer_index, correct_answer
