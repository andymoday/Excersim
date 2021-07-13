protein = {"AUG": "Methionine",
           "UUU": "Phenylalanine", "UUC": "Phenylalanine",
           "UUA": "Leucine", "UUG": "Leucine",
           "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
           "UAU": "Tyrosine", "UAC": "Tyrosine",
           "UGU": "Cysteine", "UGC": "Cysteine",
           "UGG": "Tryptophan",
           "UAA": "STOP", "UAG": "STOP", "UGA": "STOP", }


def proteins(strand):
    result = []
    while len(strand) > 0:
        if protein[strand[0:3]] == "STOP":
            return result
        else:
            result.append(protein[strand[0:3]])
            strand = strand[3:]
    return result
