import data
import utilities
import spreadsheet
import schedule
import time


def update_sheet():
    dates = utilities.get_list_of_dates(utilities.get_yesterday_date(), utilities.get_yesterday_date())

    for date in dates:
        kcal_consumed = data.get_consumed_kcal(date)
        workouts = data.get_workouts(data.get_endomondo_auth_token())
        days_workouts = data.get_days_workouts(workouts, date)

        kcal_burned = 0

        if len(days_workouts) > 0:
            kcal_burned = data.get_kcal_for_days_workouts(days_workouts)

        client = spreadsheet.create_client()
        spreadsheet.write_kcal_to_sheet(client, kcal_consumed, kcal_burned, date)

schedule.every().day.at('09:00').do(update_sheet)

while True:
    schedule.run_pending()
    time.sleep(30)