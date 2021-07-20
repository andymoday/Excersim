def find_anagrams(word, candidates):
    word = word.lower()
    return [candidate for candidate in candidates
            if sorted([char for char in candidate.lower()]) == sorted([char for char in word])
            and word != candidate.lower()]
