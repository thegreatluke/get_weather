#!/usr/bin/env python3
import argparse
import sys
import textwrap
from get_weather import location, forecast

if __name__ == '__main__':
    # Get arguments
    parser = argparse.ArgumentParser(
                    formatter_class=argparse.RawDescriptionHelpFormatter,
                    description=textwrap.dedent('''\
                       Weather forecast for a given City and State. 
                       --------------------------------------------
                             Weather data by Open-Meteo.com 
                             https://open-meteo.com/
                    '''))
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
    f = forecast(lat, long, tz)

    print("Forcast for " + l.get_city() +", " + l.get_state())
    print("Temperature => " + ''.join(str(f.get_temp()[0]))+''.join(str(f.get_temp()[1])))
    print("Feels Like  => " + ''.join(str(f.get_feels()))+''.join(str(f.get_temp()[1])))
    print("Humidity    => " + str(f.get_humid()) + "%")
    print("----------------------------------")
    print("Weather data by Open-Meteo.com")
    print("https://open-meteo.com/")