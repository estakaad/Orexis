from configparser import ConfigParser
import requests
import auth
import socket
import uuid

config_parser = ConfigParser()
config_parser.read('config.ini')

def get_consumed_kcal(date):
    bearer_token = config_parser.get('Nutridata', 'token')
    endpoint = 'https://tap.nutridata.ee/api-tap/food-diary/diary/' + str(date)
    response = requests.get(endpoint, auth=auth.BearerAuth(bearer_token))
    if 'dayMet' not in response.json():
        return 0
    else:
        return response.json()['dayMet']['consumedKcal']


def get_endomondo_auth_token():
    user = config_parser.get('Endomondo', 'user')
    password = config_parser.get('Endomondo', 'password')
    country = config_parser.get('Endomondo', 'country')
    url_authenticate = 'https://api.mobile.endomondo.com/mobile/auth'
    device_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, socket.gethostname()))

    params = {'email' : user, 'password' : password, 'deviceId' : device_id, 'action' : 'pair', 'country' : country}

    r = requests.get(url_authenticate, params=params)
    lines = r.text.split("\n")

    if lines[0] != 'OK':
        print("Request failed.")
    lines.pop(0)
    for line in lines:
        key, value = line.split("=")
        if key == "authToken":
            return value


def get_workouts(token):
    params = {'authToken' : token, 'maxResults' : 100}
    r = requests.get('http://api.mobile.endomondo.com/mobile/api/workout/list?', params=params)
    return r.json()['data']


def get_days_workouts(workouts, date):
    days_workouts = []
    for workout in workouts:
        if date in workout.get('start_time'):
            days_workouts.append(workout)
            #print('Burnt ' + str(workout.get('calories')) + ' kcal on ' + workout.get('start_time'))
    return days_workouts


def get_kcal_for_days_workouts(workouts_of_day):
    kcal = 0
    for workout in workouts_of_day:
        kcal = kcal + workout.get('calories')

    return kcal