# pylint: disable=import-error, line-too-long, invalid-name

# THE FOLLOWING IS AVAILABLE FROM THE VENV
# BUT THE LINTER HATES ITS GUTS
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
	"daily"             : ["weather_code", "temperature_2m_max", "temperature_2m_min", "sunrise", "sunset", "daylight_duration", "sunshine_duration", "uv_index_max", "uv_index_clear_sky_max", "precipitation_sum", "rain_sum", "showers_sum", "snowfall_sum", "wind_speed_10m_max", "wind_gusts_10m_max", "wind_direction_10m_dominant"],
	"temperature_unit"  : "fahrenheit",
	"wind_speed_unit"   : "mph",
	"precipitation_unit": "inch",
	"timezone"          : "America/New_York"
}
responses = openmeteo.weather_api(omurl, params=params)
forecast_for_city = responses[0]

with open(r'./OpenMateoResponses.txt', 'w') as fp:
    fp.write(f"{dir(forecast_for_city)}")
    fp.write(f"Current: {dir(forecast_for_city.Current().Variables().type())}")
    fp.write(f"Daily: {forecast_for_city.Daily()}")

# LOCATION.LATITUDE AND LOCATION.LONGITUDE GIVE ME WHAT WE NEED TO LOOKUP FROM OPEN-METEO

# print(
#     f"Address: {location.address}\n"
#     f"Coordinates: {location.latitude}, {location.longitude}\n"
#     f"Raw Data: {location.raw}\n"
# )
