from speech import say


class Speech:
    """
    Class to implement micro:bit specific speech
    """

    def __init__(self, speed=95):
        """
        Attrs:
            speed: int
        """
        self.speed = speed

    def speak(self, words):
        """
        Method to handle micro:bit speaking

        Params:
            words: str
        """
        say(words, speed=self.speed)
