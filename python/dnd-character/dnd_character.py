import random
import math


def modifier(number):
    return math.floor((number - 10) / 2)


def roll():
    rolls = []
    # four random rolls of dice
    for i in range(4):
        rolls.append(random.randint(1, 6))
    # sort highest first
    rolls.sort()
    # only return top 3
    return sum(rolls[:3])


class Character:
    def __init__(self):
        self.strength = roll()
        self.dexterity = roll()
        self.constitution = roll()
        self.intelligence = roll()
        self.wisdom = roll()
        self.charisma = roll()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return random.choice([self.strength, self.dexterity, self.constitution,
                              self.intelligence, self.wisdom, self.charisma])
