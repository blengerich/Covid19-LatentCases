def readable_date(date):
    return "{:.0f}/{:.0f}".format((date % 1e4 - date % 1e2)/1e2, date % 1e2)


def get_date_format(day, month, year):
    return year*1e4 + month*1e2 + day
