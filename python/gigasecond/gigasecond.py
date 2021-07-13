import datetime


def add(moment):
    # get difference from epoch date
    diff = moment - datetime.datetime(1970, 1, 1)
    # convert into seconds (total_seconds keeps fractional seconds intact)
    moment_in_seconds = diff.total_seconds()
    # add gigasecond
    future = moment_in_seconds + 10 ** 9
    # get utc timestamp from the future seconds value and return
    return datetime.datetime.utcfromtimestamp(future)
