from configparser import ConfigParser
import requests
import auth

config_parser = ConfigParser()
config_parser.read('config.ini')

def get_consumed_kcal(date):
    bearer_token = config_parser.get('Nutridata', 'token')
    endpoint = 'https://tap.nutridata.ee/api-tap/food-diary/diary/' + str(date)
    response = requests.get(endpoint, auth=auth.BearerAuth(bearer_token))
    return response.json()['dayMet']['consumedKcal']