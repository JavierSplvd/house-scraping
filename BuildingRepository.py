import base64
import urllib
from BuildingModel import BuildingModel
import requests

class BuildingRepository:

    def get_oauth_token():
        url: str = "https://api.idealista.com/oauth/token"
        apikey = urllib.parse.quote_plus('Provided_API_key')
        secret = urllib.parse.quote_plus('Provided_API_secret')
        auth = base64.encode(apikey + ':' + secret)
        body = {'grant_type': 'client_credentials'}
        headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
                   'Authorization': 'Basic ' + auth}

        response = requests.post(url, data=urllib.parse.urlencode(body), headers=headers)
        return response.content
