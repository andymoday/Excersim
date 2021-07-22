def primes(limit):
    all_nums = list(range(2, limit + 1))
    for num in range(2, limit + 1):
        i = 2
        multiple = 0
        while multiple <= limit:
            multiple = num * i
            if multiple in all_nums:
                all_nums.remove(multiple)
            i += 1
    return all_nums