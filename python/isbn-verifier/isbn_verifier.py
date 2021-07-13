def is_valid(isbn):
    # remove hyphens
    isbn = isbn.replace("-", "")
    # must be a ten character isbn number
    if len(isbn) != 10:
        return False
    # initialise variables
    checksum = 0
    # multiplier decreases by one for each character
    multiplier = 10
    for char in isbn:
        # False if X is not in last position(check digit) or character is not 0-9 or X
        if (char == "X" and not multiplier == 1) or (not char.isnumeric() and char != "X"):
            return False
        # X has value 10 in the formula
        char = 10 if char == "X" else char
        checksum += int(char) * multiplier
        multiplier -= 1
    return checksum % 11 == 0

