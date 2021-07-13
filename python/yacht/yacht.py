"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    total_score = 0
    # YACHT
    if category == 0:
        if dice.count(dice[0]) == 5:
            total_score += 50
    # Numbers
    elif category in (range(1, 7)):
        for die in dice:
            if die == category:
                total_score += category
    # FULL HOUSE
    elif category == 7:
        # check for only two values, with neither occuring once or four times
        if len(set(dice)) == 2 and dice.count(dice[0]) in (2, 3):
            for die in dice:
                total_score += die
    # FOUR_OF_A_KIND
    elif category == 8:
        if dice.count(dice[0]) >= 4 or dice.count(dice[1]) >= 4:
            if dice.count(dice[0]) >= 4:
                total_score += 4 * dice[0]
            else:
                total_score += 4 * dice[1]
    # LITTLE_STRAIGHT
    elif category == 9:
        if all(x in dice for x in [1, 2, 3, 4, 5]):
            total_score += 30
    # BIG_STRAIGHT
    elif category == 10:
        if all(x in dice for x in [2, 3, 4, 5, 6]):
            total_score += 30
    # CHOICE
    elif category == 11:
        for die in dice:
            total_score += die
    return total_score
