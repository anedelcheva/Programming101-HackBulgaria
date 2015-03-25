import calendar


def friday_years(start, end):
    counter = 0
    while start <= end:
        if calendar.isleap(start) and \
            (calendar.weekday(start, 1, 1) == 4 or
             calendar.weekday(start, 1, 2) == 4):
            counter += 1
        elif calendar.weekday(start, 1, 1) == 4:
            counter += 1
        start += 1
    return counter
