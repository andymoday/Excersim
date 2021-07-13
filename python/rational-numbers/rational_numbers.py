from __future__ import division


def gcd(a, b):
    # set up the higher and lower variables for gcd algorithm
    if a == b:
        return a
    elif a > b:
        higher = a
        lower = b
    else:
        higher = b
        lower = a
    # implement Euclid's GCD algorithm
    while lower != 0:
        temp = lower
        lower = higher % lower
        higher = temp
    return higher


def simplify(n, d):
    divisor = gcd(abs(n), abs(d))
    numer = int(n / divisor)
    denom = int(d / divisor)
    if denom < 0:
        numer = numer * -1
        denom = denom * -1

    return Rational(numer, denom)


class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        a = simplify(self.numer, self.denom)
        b = simplify(other.numer, other.denom)
        return a.numer == b.numer and a.denom == b.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return simplify((self.numer * other.denom + self.denom * other.numer), (self.denom * other.denom))

    def __sub__(self, other):
        return simplify((self.numer * other.denom - self.denom * other.numer), (self.denom * other.denom))

    def __mul__(self, other):
        return simplify((self.numer * other.numer), (self.denom * other.denom))

    def __truediv__(self, other):
        if (self.denom * other.numer) != 0:
            return simplify((self.numer * other.denom), (self.denom * other.numer))
        else:
            raise ValueError("Can't divide by zero")

    def __abs__(self):
        return simplify(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if isinstance(power, int) and power < 0:
            return simplify((self.denom ** abs(power)), (self.numer ** abs(power)))
        else:
            return simplify((self.numer ** power), (self.denom ** power))

    def __rpow__(self, base):
        return round((base ** self.numer) ** (1 / self.denom), 8)
