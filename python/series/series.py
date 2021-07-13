def slices(series, length):
    if length > len(series):
        raise ValueError("Length longer than series")
    elif length <= 0:
        raise ValueError("Length must be greater than zero")
    results = []
    # get a slice from each position up to the one where the length of the slice reaches the end of the series
    for i in range(len(series) - length + 1):
        results.append(series[i:i+length])
    return results
