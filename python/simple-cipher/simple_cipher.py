import secrets


class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = "".join([chr(97 + secrets.randbelow(26)) for i in range(100)])
        else:
            self.key = key

    def encode(self, text):
        return "".join([chr(97 + ((ord(text[i]) - 97 + ord(self.key[i % len(self.key)]) - 97) % 26))
                        for i in range(len(text))])

    def decode(self, text):
        return "".join([chr(97 + ((ord(text[i]) - 97) - (ord(self.key[i % len(self.key)]) - 97)) % 26)
                        for i in range(len(text))])
