# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods

# GFM :: WEATHER-VIEW
#
# CONSOLIDATES THE WEATHER INFORMATION INTO A GRAPHICAL DISPLAY

"""
WeatherView Module

Defines a view for weather information that can be inserted into a Table Cell.
"""

import ansi

class WeatherView:
    """
    Defines a WeatherView object.
    """
    def __init__(self, **kwargs) -> None:
        self.draw_offset      = kwargs['draw_offset'] if 'draw_offset' in kwargs else ansi.ATCoordinatesNone()
        self.weather_alert    = kwargs['weather_alert'] if 'weather_alert' in kwargs else None
        self.day_display      = kwargs['day_display'] if 'day_display' in kwargs else ansi.ATStringComposite()
        self.weather_art      = kwargs['weather_art'] if 'weather_art' in kwargs else []
        self.temp_display     = kwargs['temp_display'] if 'temp_display' in kwargs else ansi.ATStringComposite()
        self.humidity_display = kwargs['humidity_display'] if 'humidity_display' in kwargs else ansi.ATStringComposite()
        self.precip_display   = kwargs['precip_display'] if 'precip_display' in kwargs else ansi.ATStringComposite()

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
