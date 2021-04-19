import requests
import json

class GeocodeMock(object):

    @property
    def get(self):
        geocode_req = requests.get("https://geocoder.ls.hereapi.com/6.2/geocode.json?apiKey=YOURKEYHERE&searchtext={}")
        if geocode_req.ok:
            return geocode_req
        else:
            return None