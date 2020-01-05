import data
import utilities
import spreadsheet


dates = utilities.get_list_of_dates('2020-01-05', '2020-01-05')

for date in dates:
    kcal_consumed = data.get_consumed_kcal(date)
    workouts = data.get_workouts(data.get_endomondo_auth_token())
    days_workouts = data.get_days_workouts(workouts, date)

    kcal_burned = 0

    if len(days_workouts) > 0:
        kcal_burned = data.get_kcal_for_days_workouts(days_workouts)

    client = spreadsheet.create_client()
    spreadsheet.write_kcal_to_sheet(client, kcal_consumed, kcal_burned, date)
