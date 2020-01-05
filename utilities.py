from datetime import date, timedelta


def get_yesterday_date():
    return date.today() - timedelta(days = 1)


def iso_date_to_yyyymmdd(date):
    date = date.split()
    return date[0]