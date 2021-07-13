import random


class Robot:
    def __init__(self):
        self.name = self.make_name()

    def make_name(self):
        self.name = ""
        for i in range(2):
            num = random.randint(65, 90)
            char = chr(num)
            self.name += char
        for i in range(3):
            num = random.randint(0, 9)
            self.name += str(num)
        return self.name

    def reset(self):
        random.seed(random.randint(0, 1000))
        self.make_name()
