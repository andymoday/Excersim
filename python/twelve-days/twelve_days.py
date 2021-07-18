nth_dict = {
               1: ["first", "a Partridge in a Pear Tree."],
               2: ["second", "two Turtle Doves"],
               3: ["third", "three French Hens"],
               4: ["fourth", "four Calling Birds"],
               5: ["fifth", "five Gold Rings"],
               6: ["sixth", "six Geese-a-Laying"],
               7: ["seventh", "seven Swans-a-Swimming"],
               8: ["eighth", "eight Maids-a-Milking"],
               9: ["ninth", "nine Ladies Dancing"],
               10: ["tenth", "ten Lords-a-Leaping"],
               11: ["eleventh", "eleven Pipers Piping"],
               12: ["twelfth", "twelve Drummers Drumming"]
}


def recite(start_verse, end_verse):
    # set up output list
    output_verse = []
    # loop forward through verses
    for i in range(start_verse, end_verse + 1):
        # add first line of verse to output list
        output_verse.append(f"On the {nth_dict[i][0]} day of Christmas my true love gave to me: ")
        # loop through lines from ith line down to the first
        for j in range(i, 0, -1):
            # last line always has different punctuation
            if j == 1:
                # if outer loop contains the first verse then don't use 'and' before the last line
                if i == 1:
                    output_verse[-1] += nth_dict[j][1]
                else:
                    output_verse[-1] += f"and {nth_dict[j][1]}"
            else:
                output_verse[-1] += f"{nth_dict[j][1]}, "

    return output_verse
