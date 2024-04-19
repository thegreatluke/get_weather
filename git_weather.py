# pylint: disable=import-error, line-too-long, invalid-name

# THE FOLLOWING IS AVAILABLE FROM THE VENV
# BUT THE LINTER HATES ITS GUTS
import os
import weather_day_view as wdv
import sys
from calendar import day_abbr
import datetime
import argparse
import pdb
import pytz
import openmeteo_requests
import requests_cache
from geopy.geocoders import Nominatim
from retry_requests import retry

# pdb.set_trace()

parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description='Git Weather - Weather Git Gud'
)

# SUPPORTING INTERNATIONAL LOCATIONS WOULD REQUIRE
# CHANGING THE CALL INTERFACE
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

# USE NOMINATIM TO GEOCODE THE CITY, STATE
floc          = f"{' '.join(args.city)}, {' '.join(args.state)}"
geolocator    = Nominatim(user_agent = 'git_weather')
location      = geolocator.geocode(floc)

# BORROWED CODE FROM THE OPEN-METEO API GENERATOR
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

# PYTZ RECOMMENDS THAT TIMES BE HANDLED PRINCIPALLY AS UTC
# AND CONVERTED TO LOCALTIME FOR DISPLAY PURPOSES ONLY. WE'LL
# FOLLOW SUIT.
#
# DETERMINE THE TOTAL NUMBER OF DAYS FORECASTED BY THE API CALL.
utc_dt_start      = datetime.datetime.fromtimestamp(forecast_for_city.Daily().Time(), pytz.utc)
utc_dt_end        = datetime.datetime.fromtimestamp(forecast_for_city.Daily().TimeEnd(), pytz.utc)
num_forecast_days = utc_dt_end - utc_dt_start
dow_start_name    = day_abbr[utc_dt_start.weekday()]

# breakpoint()

# print(
#     f"Address: {location.address}\n"
#     f"Coordinates: {location.latitude}, {location.longitude}\n"
#     f"Raw Data: {location.raw}\n"
# )

# TRY TO USE THE WEATHER DAY VIEW CLASS
wdv_sample = wdv.WeatherDayView(
    weather_data=forecast_for_city.Daily()
)

os.system('cls')
print(wdv_sample)
