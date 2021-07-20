def sum_of_multiples(limit, multiples):
    numbers = []
    for multiple in multiples:
        i = 1
        while multiple * i < limit:
            numbers.append(multiple * i)
            i += 1
    return sum(numbers)

print(sum_of_multiples(100, [3, 5]))