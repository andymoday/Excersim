# Game status categories
STATUS_WIN = 1
STATUS_LOSE = -1
STATUS_ONGOING = 0


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        # arrays rather than strings for mutation
        self.word = [letter for letter in word]
        self.masked_word = ["_" for char in self.word]

    def guess(self, char):
        guess_correct = False

        if self.status == STATUS_LOSE or self.status == STATUS_WIN:
            raise ValueError("No remaining guesses")

        for i in range(len(self.word)):
            if self.word[i] == char and self.masked_word[i] != char:
                guess_correct = True
                self.masked_word[i] = char

        if not guess_correct:
            self.remaining_guesses -= 1

        if self.masked_word == self.word:
            self.status = STATUS_WIN

        if self.remaining_guesses < 0 and self.status == STATUS_ONGOING:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        return ''.join(self.masked_word)

    def get_status(self):
        return self.status
