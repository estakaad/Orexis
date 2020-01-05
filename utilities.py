from datetime import date, timedelta


def get_yesterday_date():
    return date.today() - timedelta(days = 1)