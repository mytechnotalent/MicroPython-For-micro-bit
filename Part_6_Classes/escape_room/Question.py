from random import choice
from microbit import button_a, button_b, pin_logo
from Speech import Speech
from EscapeRoomSoundEffects import EscapeRoomSoundEffects
from data import questions

speech = Speech()
sound_effects = EscapeRoomSoundEffects()


class Question:
    """
    Class to implement micro:bit specific question for escape room
    """

    @staticmethod
    def ask():
        """Method to ask a question to the player and handle logic

        Returns:
            bool
        """
        question = choice(list(questions))
        speech.speak(question)
        speech.speak('Press Ayy for {0}.'.format(questions[question][0]))
        speech.speak('Toch the logo for {0}.'.format(questions[question][1]))
        speech.speak('Press B for {0}.'.format(questions[question][2]))
        while True:
            if button_a.is_pressed():
                response = 0
                break
            elif pin_logo.is_touched():
                response = 1
                break
            elif button_b.is_pressed():
                response = 2
                break
        correct_answer = questions[question][3]
        if response == correct_answer:
            speech.speak('Correct!')
            sound_effects.play_success_sound_effect()
            return True
        else:
            speech.speak('The correct answer is {0}.'.format(questions[question][correct_answer]))
            return False
