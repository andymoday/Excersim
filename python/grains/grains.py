def square(number):
    if 65 > number > 0:
        return 2 ** (number - 1)
    else:
        raise ValueError("Please enter a number greater than zero")

def total():
    return sum([square(i) for i in range(1, 65)])
