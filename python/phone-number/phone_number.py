class PhoneNumber:
    def __init__(self, number):
        # remove standard punctuation
        number = number.replace("(", "").replace(")", "").replace("-", "").replace(".", "").replace(" ", "")
        # if number isn't 10 characters long it must be 11 characters and start with 1,
        # or 12 characters and start with + 1
        if not (len(number) == 10 or (len(number) == 11 and number[0] == "1") or
                (len(number) == 12 and number[0] == "+" and number[1] == "1")):
            raise ValueError("invalid number")
        # trim off +1 or 1 from start of number
        if len(number) > 10:
            number = number[-10:]
        # all remaining characters should be numbers
        if not number.isnumeric():
            raise ValueError("invalid number - cannot contain text or punctuation")
        # Area code and Exchange code must not start with 0 or 1
        if number[0] in ["0", "1"] or number[3] in ["0", "1"]:
            raise ValueError("area code and exchange code cannot start with 0 or 1")
        self.number = number
        self.area_code = self.number[0:3]

    def pretty(self):
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}"
