# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, too-many-instance-attributes

# GFM :: WEATHER-VIEW
#
# CONSOLIDATES THE DAILY WEATHER INFORMATION INTO A GRAPHICAL DISPLAY

"""
WeatherDayView Module

Defines a view for weather information that can be inserted into a Table Cell.
This module focuses on one day only, and from the Daily collection. The Current
Collection isn't considered.
"""

import sys
import defs
import ansi
from calendar import day_abbr
import datetime
import pytz

# VARIABLE REFERENCE DEFINITIONS
# THESE ARE PULLED FROM THE OPEN METEO API CALL
# THE ORDER IS ENTIRELY DEPENDENT UPON THE ORDER THEY
# APPEAR IN THE CALL.
APICODE_WEATHER_CODE      = 0
APICODE_TEMP2MMAX         = 1
APICODE_TEMP2MMIN         = 2
APICODE_SUNRISE           = 3
APICODE_SUNSET            = 4
APICODE_DAYLIGHT_DURATION = 5
APICODE_SUNSHINE_DURATION = 6
APICODE_WINDSPEED_10MMAX  = 7


class WeatherDayView:
    """
    Defines a WeatherView object.
    
    This expects to receive the var_name.Daily() collection as the weather_data parameter.
    """
    def __init__(self, **kwargs):
        self.weather_data = kwargs['weather_data'] if 'weather_data' in kwargs else None
        self.draw_offset  = kwargs['draw_offset'] if 'draw_offset' in kwargs else ansi.ATCoordinatesNone()
        self.day_offset   = kwargs['day_offset'] if 'day_offset' in kwargs else 0

        self.weather_code        = ansi.ATStringComposite()
        self.day_name            = ansi.ATStringComposite()
        self.weather_art         = ''
        self.temp_low            = ansi.ATStringComposite()
        self.temp_high           = ansi.ATStringComposite()
        self.sunrise             = ansi.ATStringComposite()
        self.sunset              = ansi.ATStringComposite()
        self.daylight_duration   = ansi.ATStringComposite()
        self.sunshine_duration   = ansi.ATStringComposite()
        self.windspeed_10mmax    = ansi.ATStringComposite()

    def interpolate_weather_data(self):
        if self.weather_data is not None:
            # WE CAN DO SOMETHING WITH THE DATA
            if self.draw_offset is not None:
                # SET THE CURRENT DAY
                t = datetime.datetime.fromtimestamp(self.weather_data.Time(), pytz.utc) + datetime.timedelta(days=self.day_offset)
                d = t.weekday()

                self.day_name.composite.append(
                    ansi.ATString(
                        prefix=ansi.ATStringPrefix(
                            fgcol=ansi.rainbow.CCTextDefault(),
                            coords=ansi.ATCoordinates(
                                row=self.draw_offset.row + 2,
                                col=self.draw_offset.col + 2
                            )
                        ),
                        udata=f"{day_abbr[d]} {t.day()}"
                    )
                )

                # EXAMINE THE WEATHER CODE TO DETERMINE THE TOP-LEFT ICON
                z1 = ansi.ATString(
                    prefix=ansi.ATStringPrefix(
                        coords=ansi.ATCoordinates(
                            row=self.draw_offset.row + 1,
                            col=self.draw_offset.col + 1
                        )
                    )
                )
                match self.weather_data.Variables(APICODE_WEATHER_CODE).Values(d):
                    case defs.WMO_CLEAR_SKY:
                        z1.udata        = f"{defs.UNIC_SUNNY}"
                        z1.prefix.fgcol = ansi.rainbow.CCAppleNYellowLight()
                    case defs.WMO_MAINLY_CLEAR | defs.WMO_PARTLY_CLOUDY:
                        z1.udata        = f"{defs.UNIC_SUNNY_CLOUD_MODERATE}"
                        z1.prefix.fgcol = ansi.rainbow.CCAppleNYellowALight()
                    case defs.WMO_OVERCAST:
                        z1.udata        = f"{defs.UNIC_CLOUDY}"
                        z1.prefix.fgcol = ansi.rainbow.CCAppleNGrey2Light()
                    case defs.WMO_FOG | defs.WMO_FOG_DRIME:
                        z1.udata        = f"{defs.UNIC_FOG}"
                        z1.prefix.fgcol = ansi.rainbow.CCAppleNGrey3Light()
                    case defs.WMO_DRIZZLE_LIGHT | defs.WMO_DRIZZLE_MODERATE | defs.WMO_DRIZZLE_INTENSE:
                        z1.udata        = f"{defs.UNIC_UMBRELLA}"
                        z1.prefix.fgcol = ansi.rainbow.CCAppleNPurpleLight()
                    case defs.WMO_FDRIZZLE_LIGHT | defs.WMO_FDRIZZLE_DENSE:
                        z1.udata        = f"{defs.UNIC_CLOUD_RAIN}"
                        z1.prefix.fgcol = ansi.rainbow.CCAppleNBlueLight()
                    case defs.WMO_RAIN_SLIGHT | defs.WMO_RAIN_MODERATE | defs.WMO_RAIN_HEAVY:
                        z1.udata        = f"{defs.UNIC_CLOUD_RAIN}"
                        z1.prefix.fgcol = ansi.rainbow.CCAppleNCyanLight()
                    case defs.WMO_FRAIN_LIGHT | defs.WMO_FRAIN_HEAVY:
                        z1.udata        = f"{defs.UNIC_CLOUD_RAIN}"
                        z1.prefix.fgcol = ansi.rainbow.CCAppleNMintLight()
                    case defs.WMO_SNOW_SLIGHT | defs.WMO_SNOW_MODERATE | defs.WMO_SNOW_HEAVY | defs.WMO_SNOW_GRAINS:
                        z1.udata        = f"{defs.UNIC_SNOWMAN_WSNOW}"
                        z1.prefix.fgcol = ansi.rainbow.CCWhite()
                    case defs.WMO_RSHOWERS_SLIGHT | defs.WMO_RSHOWERS_MODERATE | defs.WMO_RSHOWERS_VIOLENT:
                        z1.udata        = f"{defs.UNIC_TSTORM}"
                        z1.prefix.fgcol = ansi.rainbow.CCAppleNIndigoLight()
                
                # MIN/MAX TEMPERATURE
                self.temp_low.composite.append(
                    ansi.ATString(
                        prefix=ansi.ATStringPrefix(
                            fgcol=ansi.rainbow.CCAppleNBlueLight(),
                            coords=ansi.ATCoordinates(
                                row=self.draw_offset.row + 10,
                                col=self.draw_offset.col + 1
                            )
                        ),
                        udata=f"{defs.UNIC_THERMOMETER}"
                    )
                )
                self.temp_low.composite.append(
                    ansi.ATString(
                        prefix=ansi.ATStringPrefix(
                            fgcol=ansi.rainbow.CCTextDefault()
                        ),
                        udata=f"{self.weather_data.Variables(APICODE_TEMP2MMIN).Values(d)}{defs.UNIC_DEG_SYM}"
                    )
                )
                self.temp_high.composite.append(
                    ansi.ATString(
                        prefix=ansi.ATStringPrefix(
                            fgcol=ansi.rainbow.CCAppleNRedLight(),
                            coords=ansi.ATCoordinates(
                                row=self.draw_offset.row + 10,
                                col=self.draw_offset.col + 7
                            )
                        ),
                        udata=f"{defs.UNIC_THERMOMETER}"
                    )
                )
                self.temp_high.composite.append(
                    ansi.ATString(
                        prefix=ansi.ATStringPrefix(
                            fgcol=ansi.rainbow.CCTextDefault()
                        ),
                        udata=f"{self.weather_data.Variables(APICODE_TEMP2MMAX).Values(d)}{defs.UNIC_DEG_SYM}"
                    )
                )
                
                # SUNRISE/SUNSET
                self.sunrise.composite.append(
                    ansi.ATString(
                        prefix=ansi.ATStringPrefix(
                            fgcol=ansi.rainbow.CCAppleNYellowLight(),
                            coords=ansi.ATCoordinates(
                                row=self.draw_offset.row + 11,
                                col=self.draw_offset.col + 1
                            )
                        ),
                        udata=f"{defs.UNIC_SUNNY}"
                    )
                )
