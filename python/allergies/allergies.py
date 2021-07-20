scores = {
    "eggs": [1, -1],
    "peanuts": [2, -2],
    "shellfish": [4, -3],
    "strawberries": [8, -4],
    "tomatoes": [16, -5],
    "chocolate": [32, -6],
    "pollen": [64, -7],
    "cats": [128, -8]
}


class Allergies:

    def __init__(self, score):
        self.score = score
        self.allergies = []

    def allergic_to(self, item):
        # not allergic if no score
        if self.score == 0:
            return False
        # if score is item value exactly then allergic to the item
        elif self.score == scores[item][0]:
            return True
        # checks position of allergy value in binary representation of number
        # if 1 then the allergy is a component of the score
        else:
            try:
                return True if int(bin(self.score)[scores[item][1]]) == 1 else False
            except ValueError:
                return False
            except IndexError:
                return False

    @property
    def lst(self):
        for item in scores:
            if self.allergic_to(item):
                self.allergies.append(item)
        return self.allergies
