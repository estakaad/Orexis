from configparser import ConfigParser
import requests


config_parser = ConfigParser()
config_parser.read('config.ini')
bearer_token = config_parser.get('Nutridata', 'token')
endpoint = 'https://tap.nutridata.ee/api-tap/food-diary/diary/2020-01-04'


class BearerAuth(requests.auth.AuthBase):
    token = None
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


response = requests.get(endpoint, auth=BearerAuth(bearer_token))
print(response.json())