from random import randint


class RandomNumberGenerator:
    """
    Class to implement escape room random number generator
    """

    @staticmethod
    def generate_random_numbers():
        x = randint(1, 3)
        y = randint(1, 3)
        while x == 1 and y == 1:
            x = randint(1, 3)
            y = randint(1, 3)
        return x, y
