#!/usr/bin/env python3

import requests, json
#import requests, json, calendar
#from prettytable import PrettyTable
from datetime import date

## API VARS
header = {"User-Agent": "(rawlins.luke.weather.py luke@lukerawlins.com)"}
base_url = "https://api.weather.gov/"
zone = "OHZ055"
r = requests.get(base_url + "gridpoints/ILN/79,85/forecast", headers=header).json()
#r = requests.get(base_url + "stations/kosu/observations/latest", headers=header).json()
rhour = requests.get(base_url + "gridpoints/ILN/79,85/forecast/hourly", headers=header).json()
ralert = requests.get(base_url + "alerts/active/zone/" + zone, headers=header).json()

#today = date.today() # format like 2022-12-03
#today_num = today.weekday()
#today_week_day = calendar.day_name[today_num] # day as string (Monday, Tuesday, etc..)
#cal = calendar.setfirstweekday(today.weekday()) # set calendar first day as today
#cal = calendar.Calendar(firstweekday=today.weekday()) # set calendar first day as today

#weather_table = PrettyTable()
#weather_table.fieldnames = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

forecasts = json.loads(json.dumps(r['properties']['periods']))
hour_cast = json.loads(json.dumps(rhour['properties']['periods']))
cast_list = []
print("------------------------------")
for cast in hour_cast:
    if cast['number'] <= 12:
        cast_list.append(cast['temperature'])

print("Next 12 hours: " + str(cast_list[0:]))
for forecast in forecasts:
    if forecast['number'] <= 4:
        print("Forecast for: "+forecast['name'])
        print("Tempurature: "+str(forecast['temperature']) + forecast['temperatureUnit'])
        print("Wind Speed: " + forecast['windSpeed'] + ", direction " + forecast['windDirection'])
        print(forecast['detailedForecast'])
        print("------------------------------")
#cal_day_names = []
#for day in cal.iterweekdays():
#    if day == 0:
#        day = "Monday"
#        cal_day_names.append(day)
#    elif day == 1:
#        day = "Tuesday"
#        cal_day_names.append(day)
#    elif day == 2:
#        day = "Wednesday"
#        cal_day_names.append(day)
#    elif day == 3:
#        day = "Thursday"
#        cal_day_names.append(day)
#    elif day == 4:
#        day = "Friday"
#        cal_day_names.append(day)
#    elif day == 5:
#        day = "Saturday"
#        cal_day_names.append(day)
#    elif day == 6:
#        day = "Sunday"
#        cal_day_names.append(day)
#    else:
#        print("This is embarassing... something is wrong")
##weather_table.field_names = cal_day_names
#table_dict = {}
#for i in cal_day_names:
#    for forecast in forecasts:
#        if i == forecast['name']:
#            cast_name = forecast['name']
#            cast_temp = forecast['temperature']
#            cast_wind = forecast['windSpeed']
#            cast_wind_dir = forecast['windDirection']
#            cast_detail = forecast['detailedForecast']
#            #table_dict[i] = {day=cast_name,temp=cast_temp,wind=cast_wind,wind_dir=cast_wind_dir,detail=cast_detail} 
#            weather_table.add_column(i,[
#                                     cast_name,
#                                     cast_temp,
#                                     cast_wind+cast_wind_dir,
#                                     cast_detail
#                              ]) 
#print(table_dict)
#print(weather_table)
alerts = json.loads(json.dumps(ralert))
if alerts['features']:
    #print(alerts['features'])
    for alert in alerts['features']:
        sender = json.dumps(alert['properties']['senderName'])
        headline = json.dumps(alert['properties']['headline'])
        description = json.dumps(alert['properties']['description'])
        print("Weather Alerts!!!")
        print("from: " + sender)
        print(headline)
        print(description)
        print("------------------------------")
        #print(json.dumps(alert, indent=4))

#print(weather_table)
#print(json.dumps(rhour, indent=4))
#print(json.dumps(ralert, indent=4))
#print(json.dumps(r, indent=4))
