# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, too-many-instance-attributes

# GFM :: WEATHER-VIEW
#
# CONSOLIDATES THE WEATHER INFORMATION INTO A GRAPHICAL DISPLAY

"""
WeatherView Module

Defines a view for weather information that can be inserted into a Table Cell.
"""

import sys
import ansi

class WeatherView:
    """
    Defines a WeatherView object.
    """
    def __init__(self, **kwargs) -> None:
        self.weather_data     = kwargs['weather_data'] if 'weather_data' in kwargs else None
        self.draw_offset      = kwargs['draw_offset'] if 'draw_offset' in kwargs else ansi.ATCoordinatesNone()
        self.weather_alert    = kwargs['weather_alert'] if 'weather_alert' in kwargs else None
        self.day_display      = kwargs['day_display'] if 'day_display' in kwargs else ansi.ATStringComposite()
        self.weather_art      = kwargs['weather_art'] if 'weather_art' in kwargs else []
        self.temp_display     = kwargs['temp_display'] if 'temp_display' in kwargs else ansi.ATStringComposite()
        self.humidity_display = kwargs['humidity_display'] if 'humidity_display' in kwargs else ansi.ATStringComposite()
        self.precip_display   = kwargs['precip_display'] if 'precip_display' in kwargs else ansi.ATStringComposite()

    def interpolate_weather_data(self) -> None:
        if self.weather_data is not None:
            # WE CAN DO SOMETHING WITH THE DATA
            # ASSUME THAT THIS IS THE JSON-CONVERTED OBJECT
            # CHECK TO SEE IF THE DRAW OFFSET HAS BEEN SET
            # OTHERWISE, WE CAN'T DO MUCH HERE (THROW -99)
            if self.draw_offset is not None:
                pass
            else:
                sys.exit(-99)

    def draw(self) -> str:
        """
        Populates the data from this view into a string with ANSI SGRs and returns that to the caller.
        """
        a = ''

        a += f"{ansi.ATCoordinates(row = (self.draw_offset.row + 1), col = (self.draw_offset.col + 1)).to_ansi_str()}{self.weather_alert.to_ansi_str()}"
        a += f"{ansi.ATCoordinates(row = (self.draw_offset.row + 2), col = (self.draw_offset.col + 2)).to_ansi_str()}{self.day_display.to_ansi_str()}"
        a += f"{ansi.ATCoordinates(row = (self.draw_offset.row + 4), col = (self.draw_offset.col + 1)).to_ansi_str()}{self.weather_art}"
        a += f"{ansi.ATCoordinates(row = (self.draw_offset.row + 10), col = (self.draw_offset.col + 1)).to_ansi_str()}{self.temp_display.to_ansi_str()}"
        a += f"{ansi.ATCoordinates(row = (self.draw_offset.row + 10), col = (self.draw_offset.col + 7)).to_ansi_str()}{self.humidity_display.to_ansi_str()}"
        a += f"{ansi.ATCoordinates(row = (self.draw_offset.row + 11), col = (self.draw_offset.col + 1)).to_ansi_str()}{self.precip_display.to_ansi_str()}"

        return a
