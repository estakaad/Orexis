import data
import utilities

#yesterday = str(utilities.get_yesterday_date())
yesterday = '2020-01-04'

kcal_consumed = data.get_consumed_kcal(yesterday)

workouts = data.get_workouts(data.get_endomondo_auth_token())
days_workouts = data.get_days_workouts(workouts, yesterday)

kcal_burned = 0

if len(days_workouts) > 0:
    kcal_burned = data.get_kcal_for_days_workouts(days_workouts)

print(str(kcal_consumed))
print(str(kcal_burned))