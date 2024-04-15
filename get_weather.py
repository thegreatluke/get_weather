#!/usr/bin/env python3
import argparse
import json
import sys
import textwrap
import requests

class location():
    def __init__(self, city, state):
        self.city = city.title()
        self.state = state.title()
        print(self.city + ', ' +  self.state)
        self.geo_url='https://geocoding-api.open-meteo.com/v1/search'
        self.params = {
            "name": self.city,
            "count": 10,
        }
        try:
            r = requests.get(self.geo_url, params=self.params)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        for i in r.json()['results']:
            #print(json.dumps(r.json(),indent=4))
            if i['admin1'] == self.state:
                self.lat = i['latitude']
                self.long = i['longitude']
                self.tz = i['timezone']
                self.country = i['country']
                break
            else:
                continue

    def get_lat(self):
        try:
            self.lat
        except NameError as e:
            raise SystemExit(e)
        return self.lat

    def get_long(self):
        try:
            self.long
        except NameError as e:
            raise SystemExit(e)
        return self.long

    def get_tz(self):
        try:
            self.tz
        except NameError as e:
            raise SystemExit(e)
        return self.tz

    def get_country(self):
        try:
            self.country
        except NameError as e:
            raise SystemExit(e)
        return self.country

class forecast():
    def __init__(self, lat, long, tz):
        self.w_url = 'https://api.open-meteo.com/v1/forecast'
        self.api_lic = 'Weather data by Open-Meteo.com'
        self.api_lnk = 'https://open-meteo.com/'
        self.params = {
            "latitude": lat,
            "longitude": long,
            "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,rain,showers,snowfall,cloud_cover",
            #rain,showers,snowfall,cloud_cover,wind_speed_10m,wind_direction_10m,wind_gusts_10"
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "precipitation_unit": "inch",
            #"minutely_15": "wind_speed_10m",
            "timezone": tz,
            #"past_days": 1,
        }
        try:
            self.r = requests.get(self.w_url, params=self.params)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def get_forecast(self):
        print(self.api_lic)
        print(self.api_lnk)
        return self.r.json()

parser = argparse.ArgumentParser(
                    formatter_class=argparse.RawDescriptionHelpFormatter,
                    description=textwrap.dedent('''\
                       Weather forecast for a given City and State. 
                       --------------------------------------------
                             Weather data by Open-Meteo.com 
                             https://open-meteo.com/
                    '''))
# Get arguments
parser.add_argument("-c", "--city", help="A City, example: Columbus", nargs='+', required=True)
parser.add_argument("-s", "--state", help="A State, example: Ohio", nargs ='+', required=True)
args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

# If the city/state are two words need to turn the list into a two word string
city = ' '.join(args.city)
state = ' '.join(args.state)
# create location class passing in city and state
## Todo: make it international
l = location(city, state)
lat = l.get_lat()
long = l.get_long()
tz = l.get_tz()
# Finally pass in latitude and longitude to get forecast
f = forecast(lat, long, tz).get_forecast()
## Todo: parse this json and print something nicer.
print(json.dumps(f,indent=4))


