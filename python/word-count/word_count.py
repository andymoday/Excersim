import string


def count_words(sentence):
    sentence_word_counts = {}

    # gets list of all punctuation characters, removes apostrophe (dealt with later), and stores in dictionary
    punc = string.punctuation.replace("'", "")
    punc_dict = str.maketrans('', '', punc)
    # makes all values in dictionary into space key
    for key in punc_dict:
        punc_dict[key] = 32
    # changes all characters in the sentence that appear in the dictionary into spaces
    # (catches words where there are no spaces, only punctuation)
    sentence = sentence.translate(punc_dict)

    # convert to lowercase and split on whitespace
    sentence_word_list = sentence.lower().split()

    # deal with apostrophe by stripping any occurrences at beginning and end of each word
    # (leaves any appearing mid word as contractions)
    for i in range(len(sentence_word_list)):
        if sentence_word_list[i].count("'") != 0:
            sentence_word_list[i] = sentence_word_list[i].strip("'")

    # loop through word list, adding the word or updating the count
    for word in sentence_word_list:
        if word not in sentence_word_counts.keys():
            sentence_word_counts[word] = 1
        else:
            sentence_word_counts[word] += 1

    return sentence_word_counts
