# get_weather

`get_weather.py` is a command line script that uses the Open-Meteo api for both geolocation and weather information.

## Usage:

`get_weather.py` requires two parameters city and state.

Example: `./get_weather.py -c Columbus -s Ohio`

### Example output:

```
 ~/projects/get_weather/ [main*] ./get_weather.py -c columbus -s ohio
Forcast for Columbus, Ohio
Temperature => 78.6°F
Feels Like  => 80.7°F
Humidity    => 42%
----------------------------------
Weather data by Open-Meteo.com
https://open-meteo.com/
```

## Requirements

Python 3 with the requests library installed.



