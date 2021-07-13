class Matrix:
    def __init__(self, matrix_string):
        # splits matrix_string into array of row arrays on the newline character
        # for each row array, split elements on the space character and convert to ints
        self.matrix = [[int(item) for item in row.split(" ")] for row in matrix_string.split("\n")]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.matrix]
