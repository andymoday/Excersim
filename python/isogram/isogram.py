def is_isogram(string):
    # ensuring case is irrelevant in character count
    string = string.lower()
    for char in string:
        # excludes whitespace, punctuation etc.
        if string.count(char) > 1 and char.isalpha():
            return False
    return True
