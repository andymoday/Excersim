import math


def factors(value):
    prime_factors = []
    # While value is divisible by 2, add to list of prime factors and divide value by 2.
    while value % 2 == 0:
        prime_factors.append(2)
        value /= 2
    # Now value must be odd. Loop from i = 3 to square root of n.
    # While i divides value, add i to list of prime factors and divide value by i.
    # After i fails to divide value, increment i by 2 through the odd numbers and continue.
    for i in range(3, round(math.sqrt(value)) + 1):
        while value % i == 0:
            prime_factors.append(i)
            value /= i
        i += 2
    # If value is a prime number and is greater than 2, then value will not become 1 by above two steps.
    # Hence add value to prime factors if it is greater than 2. '
    if value > 2:
        prime_factors.append(int(value))
    return prime_factors
