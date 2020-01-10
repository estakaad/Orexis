from datetime import date, timedelta, datetime
import schedule
import time
import data


def date_str_to_obj(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').date()


def get_yesterday_date():
    return date.today() - timedelta(days = 1)


def get_previous_date(date_str):
    date_object = date_str_to_obj(date_str)
    return date_object - timedelta(days = 1)


def get_next_date(date_str):
    date_object = date_str_to_obj(date_str)
    return  date_object + timedelta(days= 1)


def iso_date_to_yyyymmdd(iso_date):
    iso_date = iso_date.split()
    return iso_date[0]


def date_str_to_timestamp(date_obj):
    date_time = datetime.combine(date_obj, datetime.min.time())
    return int(datetime.timestamp(date_time))


def timestamp_to_date(timestamp):
    return datetime.date.fromtimestamp(timestamp)


def get_list_of_dates(start_date, end_date):
    start_date = date(*map(int, start_date.split('-')))
    end_date = date(*map(int, end_date.split('-')))
    delta = timedelta(days=1)
    dates = []
    while start_date <= end_date:
        dates.append(start_date.strftime("%Y-%m-%d"))
        start_date += delta
    return dates


# Time of day as string hh:mm
def scheduler(time_of_day):
    schedule.every().day.at(time_of_day).do(data.update_sheet)

    while True:
        schedule.run_pending()
        time.sleep(30)