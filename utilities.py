from datetime import date, timedelta


def get_yesterday_date():
    return date.today() - timedelta(days = 1)


def iso_date_to_yyyymmdd(date):
    date = date.split()
    return date[0]


def get_list_of_dates(start_date, end_date):
    start_date = date(*map(int, start_date.split('-')))
    end_date = date(*map(int, end_date.split('-')))
    delta = timedelta(days=1)
    dates = []
    while start_date <= end_date:
        dates.append(start_date.strftime("%Y-%m-%d"))
        start_date += delta
    return dates