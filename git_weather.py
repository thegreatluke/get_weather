#!/usr/bin/env python3
# pylint: disable=import-error, line-too-long, invalid-name

import os
import weather_table as wtbl
import sys
import argparse
import openmeteo_requests
import requests_cache
from geopy.geocoders import Nominatim
from retry_requests import retry

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='Git Weather - Weather Git Gud'
)

parser.add_argument(
    '-c',
    '--city',
    help     = 'The name of a US City',
    nargs    = '+',
    required = True
)
parser.add_argument(
    '-s',
    '--state',
    help     = 'The name of a US State',
    nargs    = '+',
    required = True
)
args = parser.parse_args(
    args = None if sys.argv[1:] else ['--help']
)

floc          = f"{' '.join(args.city)}, {' '.join(args.state)}"
geolocator    = Nominatim(user_agent = 'git_weather')
location      = geolocator.geocode(floc)
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo     = openmeteo_requests.Client(session = retry_session)
omurl         = "https://api.open-meteo.com/v1/forecast"
params        = {
	"latitude"          : location.latitude,
	"longitude"         : location.longitude,
	"current"           : ["temperature_2m", "is_day", "precipitation", "rain", "showers", "snowfall", "weather_code", "cloud_cover", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m"],
	"daily"             : ["weather_code", "temperature_2m_max", "temperature_2m_min", "sunrise", "sunset", "daylight_duration", "sunshine_duration", "wind_speed_10m_max"],
	"temperature_unit"  : "fahrenheit",
	"wind_speed_unit"   : "mph",
	"precipitation_unit": "inch",
	"timezone"          : "America/New_York"
}
responses         = openmeteo.weather_api(omurl, params = params)
forecast_for_city = responses[0]
weather_table     = wtbl.WeatherTable(
    weather_data=forecast_for_city.Daily()
)

os.system('cls')
print(weather_table)
print("\n\n\n")
