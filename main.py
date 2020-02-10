import data
import utilities
import spreadsheet
import logging


#logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p',
#                    filename= utilities.current_date_and_time_as_string() + '-log.log', level=logging.INFO)

dates = utilities.get_list_of_dates('2020-02-08', '2020-02-08')
health_parameters = ['weight', 'bodyFat', 'bodyWater', 'boneMass', 'muscleMass']


def get_nutridata_info_for_spreadsheet(date):
    kcal_consumed = data.get_consumed_kcal(date)

    return kcal_consumed


def get_endomondo_data_for_spreadsheet(date):
    workouts = data.get_workouts(data.get_endomondo_auth_token())
    days_workouts = data.get_days_workouts(workouts, date)

    kcal_burned = 0

    if len(days_workouts) > 0:
        kcal_burned = data.get_kcal_for_days_workouts(days_workouts)

    return kcal_burned


def get_garmin_data_for_spreadsheet(garmin_health_parameter_names, date):
    health_values = {}

    for parameter_name in garmin_health_parameter_names:
        health_values[parameter_name] = data.get_days_health_data(data.get_health_data(), parameter_name, date)

    return health_values


def update_sheet(list_of_dates, garmin_health_parameter_names):

    for date in list_of_dates:
        print(date)
        kcal_in = get_nutridata_info_for_spreadsheet(date)
        print('Nutridata kcal: ' + str(kcal_in))
        kcal_out = get_endomondo_data_for_spreadsheet(date)
        print('Endomondo kcal: ' + str(kcal_out))
        health_parameters = get_garmin_data_for_spreadsheet(garmin_health_parameter_names, date)
        client = spreadsheet.create_client()
        spreadsheet.write_data_to_sheet(client, kcal_in, kcal_out, health_parameters["weight"] / 1000,
                                        health_parameters["bodyFat"], health_parameters["bodyWater"],
                                        health_parameters["boneMass"] / 1000, health_parameters["muscleMass"] / 1000,
                                        date)
        print('Weight: ' + str(health_parameters["weight"] / 1000))
        print('Body fat: ' + str(health_parameters["bodyFat"]))
        print('Body water: ' + str(health_parameters["bodyWater"]))
        print('Bone mass: ' + str(health_parameters["boneMass"] / 1000))
        print('Muscle mass: ' + str(health_parameters["muscleMass"] / 1000))


update_sheet(dates, health_parameters)