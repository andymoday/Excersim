def is_pangram(sentence):
    # make dictionary of a-z (ASCII 97 - 122)
    a_z_dict = {chr(ASCII): False for ASCII in range(97, 123)}
    # remove spaces and convert to lowercase. marks each character from the sentence as present in the dictionary
    for char in sentence.lower():
        if char in a_z_dict.keys():
            a_z_dict[char] = True
    # check entries in dictionary. if any value is not present then return False as the answer
    for key in a_z_dict:
        if not a_z_dict[key]:
            return False
    # otherwise all values are True and all characters are present so return True as the answer
    return True
