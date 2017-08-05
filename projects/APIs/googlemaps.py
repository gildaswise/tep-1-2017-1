# Uso via terminal: python googlemaps.py <api_key> "<endereco>"

from sys import argv
import requests
import json

script, first, second = argv

def get_geocode_location(input_str):
    google_api_key = first
    location_string = input_str.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % 
    (location_string, google_api_key))
    response = requests.get(url)
    result = response.json()
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude, longitude)

print(get_geocode_location(second))