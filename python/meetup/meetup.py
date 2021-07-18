import datetime as dt
from calendar import monthrange

day_dict: dict = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}


class MeetupDayException(Exception):
    pass


def meetup(year, month, week, day_of_week):

    # Get weekday of the first calendar day in the month and the number of days in the month using monthrange
    first_of_month_weekday: int = monthrange(year, month)[0]
    days_in_month: int = monthrange(year, month)[1]

    # Get the date of the first occurrence of the requested weekday in the month
    diff: int = day_dict[day_of_week] - first_of_month_weekday
    if diff >= 0:
        day: int = diff + 1
    else:
        day: int = 8 + diff

    # Add the relevant amount of weeks to the first occurence of the requested weekday in the month
    if week == "2nd":
        day += 7
    elif week == "3rd":
        day += 14
    elif week == "4th":
        day += 21
    elif week == "5th":
        day += 28
        if day > days_in_month:
            raise MeetupDayException("No day exists for this weekday in this month")
    elif week == "teenth":
        # this will work if first occurence > 6th
        day += 7
        # for everything else it will be another week later
        if day < 13:
            day += 7
    elif week == "last":
        # check for 5 week months
        day += 28
        # otherwise it will be a week earlier
        if day > days_in_month:
            day -= 7

    return dt.date(year, month, day)
