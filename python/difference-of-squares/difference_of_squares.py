def square_of_sum(number: int):
    sum: int = 0
    while number > 0:
        sum += number
        number -= 1
    return sum ** 2


def sum_of_squares(number: int):
    sum: int = 0
    while number > 0:
        square: int = number ** 2
        sum += square
        number -= 1
    return sum


def difference_of_squares(number: int):
    return square_of_sum(number) - sum_of_squares(number)
