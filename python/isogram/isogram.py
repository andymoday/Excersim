def is_isogram(string):
    for char in string:
        if string.count(char) > 1:
            return False
    return True
