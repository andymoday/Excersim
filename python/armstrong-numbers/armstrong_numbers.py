def is_armstrong_number(number):
    # convert to string to iterate over and calculate number of digits
    digits = str(number)
    num_digits = len(digits)
    total = 0
    # iterate over digits, calculating the result of the equation
    for char in digits:
        total += int(char) ** num_digits
    # if number is Armstrong number then return True
    if total == number:
        return True
    return False


