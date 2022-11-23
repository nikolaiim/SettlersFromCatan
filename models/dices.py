import random

class Dices:
    @staticmethod
    def throw():
        return random.randint(1,6) + random.randint(1,6)