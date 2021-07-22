def sum_of_multiples(limit, multiples):
    numbers = []
    for multiple in multiples:
        if multiple == 0:
            continue
        i = 1
        while multiple * i < limit:
            if multiple * i not in numbers:
                numbers.append(multiple * i)
            i += 1
    return sum(numbers)
