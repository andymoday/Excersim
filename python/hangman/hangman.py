# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked_word = ''.join(["_" for char in self.word])

    def guess(self, char):
        if self.remaining_guesses == 0:
            self.status = STATUS_LOSE
            raise ValueError  # ("No remaining guesses")

        self.masked_word = ""
        for letter in self.word:
            if letter == char:
                guess_correct = True
                self.masked_word += char
            else:
                self.masked_word += "_"

        if self.masked_word == self.word:
            self.status = STATUS_WIN

        if guess_correct:
            self.remaining_guesses -= 1

        guess_correct = False

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status

