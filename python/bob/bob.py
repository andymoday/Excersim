def response(hey_bob):
    if hey_bob.isupper() and "?" in hey_bob:
        return 'Calm down, I know what I\'m doing!'
    elif hey_bob.isupper():
        return 'Whoa, chill out!'
    elif "?" == hey_bob[-1]:
        return "Sure."
    elif hey_bob == "":
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'

# print(response("Ending with ? means a question."))