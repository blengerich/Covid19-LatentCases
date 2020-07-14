def readable_date(date):
    return "{:.0f}/{:.0f}".format((date % 1e4 - date % 1e2)/1e2, date % 1e2)


def get_date_format(day, month, year):
    return year*1e4 + month*1e2 + day


dates = [get_date_format(d, 3, 2020) for d in range(16, 32)] # March dates (before the 16th many states did not report negative test counts)
dates.extend([get_date_format(d, 4, 2020) for d in range(1, 31)]) # April dates
dates.extend([get_date_format(d, 5, 2020) for d in range(1, 32)]) # May dates
dates.extend([get_date_format(d, 6, 2020) for d in range(1, 31)]) # June dates
dates.extend([get_date_format(d, 7, 2020) for d in range(1, 14)]) # July dates
readable_dates = list(map(readable_date, dates))