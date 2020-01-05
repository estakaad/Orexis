import data
import utilities
import spreadsheet

#yesterday = str(utilities.get_yesterday_date())
yesterday = '2020-01-04'

kcal_consumed = data.get_consumed_kcal(yesterday)

workouts = data.get_workouts(data.get_endomondo_auth_token())
days_workouts = data.get_days_workouts(workouts, yesterday)

kcal_burned = 0

if len(days_workouts) > 0:
    kcal_burned = data.get_kcal_for_days_workouts(days_workouts)


client = spreadsheet.create_client()
spreadsheet.write_kcal_to_sheet(client, kcal_consumed, kcal_burned, yesterday)
