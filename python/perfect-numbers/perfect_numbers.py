import math


def classify(number):

    if number <= 0:
        raise ValueError("Must enter a positive number")
    # edge case - can't include number itself in aliquot sum
    if number == 1:
        return "deficient"

    # excludes number itself from results by starting range from 2
    aliquot_sum = 1

    # one of each pair of divisors is found between 0 and sqrt. Sqrt may not be integer so need to round
    # add one to include the squareroot if it is an integer
    for i in range(2, round(math.sqrt(number)) + 1):
        # this catches divisors up to and including sqrt
        if number % i == 0:
            # if it is the sqrt, only include once
            if number / i == i:
                aliquot_sum += i
            # otherwise include the divisor and it's pair (number/divisor)
            else:
                aliquot_sum += number / i
                aliquot_sum += i

    # classification
    return "abundant" if aliquot_sum > number else "deficient" if aliquot_sum < number else "perfect"
