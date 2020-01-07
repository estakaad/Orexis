import data
import utilities
import spreadsheet
import schedule
import time


def update_sheet():
    dates = utilities.get_list_of_dates('2020-01-03', '2020-01-04')

    for date in dates:
        kcal_consumed = data.get_consumed_kcal(date)
        workouts = data.get_workouts(data.get_endomondo_auth_token())
        days_workouts = data.get_days_workouts(workouts, date)

        kcal_burned = 0

        if len(days_workouts) > 0:
            kcal_burned = data.get_kcal_for_days_workouts(days_workouts)

        weight = data.get_days_health_data(data.get_health_data(), 'weight', date)
        fat = data.get_days_health_data(data.get_health_data(), 'bodyFat', date)
        water = data.get_days_health_data(data.get_health_data(), 'bodyWater', date)
        bone = data.get_days_health_data(data.get_health_data(), 'boneMass', date)
        muscle = data.get_days_health_data(data.get_health_data(), 'muscleMass', date)

        client = spreadsheet.create_client()
        spreadsheet.write_data_to_sheet(client, kcal_consumed, kcal_burned, weight, fat, water, bone, muscle, date)

update_sheet()