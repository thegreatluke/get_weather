# pylint: disable=line-too-long, superfluous-parens, too-few-public-methods, too-many-instance-attributes

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
        self.draw_offset  = kwargs['draw_offset'] if 'draw_offset' in kwargs else ansi.ATCoordinatesDefault()
        self.day_offset   = kwargs['day_offset'] if 'day_offset' in kwargs else 0

        self.weather_code      = ansi.ATStringComposite()
        self.day_name          = ansi.ATStringComposite()
        self.temp_low          = ansi.ATStringComposite()
        self.temp_high         = ansi.ATStringComposite()
        self.sunrise           = ansi.ATStringComposite()
        self.sunset            = ansi.ATStringComposite()
        self.daylight_duration = ansi.ATStringComposite()
        self.sunshine_duration = ansi.ATStringComposite()
        self.windspeed_10mmax  = ansi.ATStringComposite()

        self.interpolate_weather_data()

    def __str__(self) -> str:
        return f"{self.weather_code.to_ansi_str()} \
            {self.windspeed_10mmax.to_ansi_str()} \
            {self.day_name.to_ansi_str()} \
            {self.temp_low.to_ansi_str()} \
            {self.temp_high.to_ansi_str()}"

    def interpolate_weather_data(self):
        """
        Takes the weather data provided from the data set and interpolates it into the desired layout.
        """
        if self.weather_data is not None:
            # WE CAN DO SOMETHING WITH THE DATA
            if self.draw_offset is not None:
                # SET THE CURRENT DAY
                t = datetime.datetime.fromtimestamp(self.weather_data.Time(), pytz.utc) + datetime.timedelta(days=self.day_offset)
                d = t.weekday()

                # EXAMINE THE WEATHER CODE TO DETERMINE THE TOP-LEFT ICON
                self.weather_code = ansi.ATString(
                    prefix=ansi.ATStringPrefix(
                        coords=ansi.ATCoordinates(
                            row=self.draw_offset.row + 1,
                            col=self.draw_offset.col + 1
                        )
                    )
                )
                match self.weather_data.Variables(APICODE_WEATHER_CODE).Values(0):
                    case defs.WMO_CLEAR_SKY:
                        self.weather_code.udata        = f"{defs.UNIC_SUNNY}"
                        self.weather_code.prefix.fgcol = ansi.rainbow.CCAppleNYellowLight()
                    case defs.WMO_MAINLY_CLEAR | defs.WMO_PARTLY_CLOUDY:
                        self.weather_code.udata        = f"{defs.UNIC_SUNNY_CLOUD_MODERATE}"
                        self.weather_code.prefix.fgcol = ansi.rainbow.CCAppleNYellowALight()
                    case defs.WMO_OVERCAST:
                        self.weather_code.udata        = f"{defs.UNIC_CLOUDY}"
                        self.weather_code.prefix.fgcol = ansi.rainbow.CCAppleNGrey2Light()
                    case defs.WMO_FOG | defs.WMO_FOG_DRIME:
                        self.weather_code.udata        = f"{defs.UNIC_FOG}"
                        self.weather_code.prefix.fgcol = ansi.rainbow.CCAppleNGrey3Light()
                    case defs.WMO_DRIZZLE_LIGHT | defs.WMO_DRIZZLE_MODERATE | defs.WMO_DRIZZLE_INTENSE:
                        self.weather_code.udata        = f"{defs.UNIC_UMBRELLA}"
                        self.weather_code.prefix.fgcol = ansi.rainbow.CCAppleNPurpleLight()
                    case defs.WMO_FDRIZZLE_LIGHT | defs.WMO_FDRIZZLE_DENSE:
                        self.weather_code.udata        = f"{defs.UNIC_CLOUD_RAIN}"
                        self.weather_code.prefix.fgcol = ansi.rainbow.CCAppleNBlueLight()
                    case defs.WMO_RAIN_SLIGHT | defs.WMO_RAIN_MODERATE | defs.WMO_RAIN_HEAVY:
                        self.weather_code.udata        = f"{defs.UNIC_CLOUD_RAIN}"
                        self.weather_code.prefix.fgcol = ansi.rainbow.CCAppleNCyanLight()
                    case defs.WMO_FRAIN_LIGHT | defs.WMO_FRAIN_HEAVY:
                        self.weather_code.udata        = f"{defs.UNIC_CLOUD_RAIN}"
                        self.weather_code.prefix.fgcol = ansi.rainbow.CCAppleNMintLight()
                    case defs.WMO_SNOW_SLIGHT | defs.WMO_SNOW_MODERATE | defs.WMO_SNOW_HEAVY | defs.WMO_SNOW_GRAINS:
                        self.weather_code.udata        = f"{defs.UNIC_SNOWMAN_WSNOW}"
                        self.weather_code.prefix.fgcol = ansi.rainbow.CCWhite()
                    case defs.WMO_RSHOWERS_SLIGHT | defs.WMO_RSHOWERS_MODERATE | defs.WMO_RSHOWERS_VIOLENT:
                        self.weather_code.udata        = f"{defs.UNIC_TSTORM}"
                        self.weather_code.prefix.fgcol = ansi.rainbow.CCAppleNIndigoLight()

                # DAY NAME
                self.day_name.composite.append(
                    ansi.ATString(
                        prefix=ansi.ATStringPrefix(
                            fgcol=ansi.rainbow.CCTextDefault(),
                            coords=ansi.ATCoordinates(
                                row=self.draw_offset.row + 1,
                                col=self.weather_code.prefix.coords.col + 3
                            )
                        ),
                        udata=f"{day_abbr[d]} {t.day}"
                    )
                )

                # WINDSPEED
                self.windspeed_10mmax.composite.append(
                    ansi.ATString(
                        prefix=ansi.ATStringPrefix(
                            fgcol=ansi.rainbow.CCTextDefault(),
                            coords=ansi.ATCoordinates(
                                row=self.draw_offset.row + 2,
                                col=self.draw_offset.col + 1
                            )
                        ),
                        udata=f"{defs.UNIC_WIND}"
                    )
                )
                self.windspeed_10mmax.composite.append(
                    ansi.ATString(
                        prefix=ansi.ATStringPrefix(
                            fgcol=ansi.rainbow.CCTextDefault(),
                            coords=ansi.ATCoordinates(
                                row=self.draw_offset.row + 2,
                                col=self.windspeed_10mmax.composite[0].prefix.coords.col + 3
                            )
                        ),
                        udata=f"{int(self.weather_data.Variables(APICODE_WINDSPEED_10MMAX).Values(0))} Mph"
                    )
                )

                # MIN/MAX TEMPERATURE
                self.temp_low.composite.append(
                    ansi.ATString(
                        prefix=ansi.ATStringPrefix(
                            fgcol=ansi.rainbow.CCAppleNBlueLight(),
                            coords=ansi.ATCoordinates(
                                row=self.draw_offset.row + 3,
                                col=self.draw_offset.col + 1
                            )
                        ),
                        udata=f"{defs.UNIC_TEMP_LOW}"
                    )
                )
                self.temp_low.composite.append(
                    ansi.ATString(
                        prefix=ansi.ATStringPrefix(
                            fgcol=ansi.rainbow.CCTextDefault(),
                            coords=ansi.ATCoordinates(
                                row=self.draw_offset.row + 3,
                                col=self.temp_low.composite[0].prefix.coords.col + 2
                            )
                        ),
                        udata=f"{int(self.weather_data.Variables(APICODE_TEMP2MMIN).Values(0)):03}{defs.UNIC_DEG_SYM}"
                    )
                )
                self.temp_high.composite.append(
                    ansi.ATString(
                        prefix=ansi.ATStringPrefix(
                            fgcol=ansi.rainbow.CCAppleNRedLight(),
                            coords=ansi.ATCoordinates(
                                row=self.draw_offset.row + 3,
                                col=self.draw_offset.col + 8
                            )
                        ),
                        udata=f"{defs.UNIC_TEMP_HIGH}"
                    )
                )
                self.temp_high.composite.append(
                    ansi.ATString(
                        prefix=ansi.ATStringPrefix(
                            fgcol=ansi.rainbow.CCTextDefault(),
                            coords=ansi.ATCoordinates(
                                row=self.draw_offset.row + 3,
                                col=self.temp_high.composite[0].prefix.coords.col + 2
                            )
                        ),
                        udata=f"{int(self.weather_data.Variables(APICODE_TEMP2MMAX).Values(0)):03}{defs.UNIC_DEG_SYM}"
                    )
                )

                # SUNRISE/SUNSET
                # THESE AREN'T GENERATING ANY DATA FROM THE API CALL
                # I REALLY SHOULD ADD CASES FOR MISSING DATA, BUT I'M
                # LAZY AS FUCK.
                # self.sunrise.composite.append(
                #     ansi.ATString(
                #         prefix=ansi.ATStringPrefix(
                #             fgcol=ansi.rainbow.CCAppleNYellowLight(),
                #             coords=ansi.ATCoordinates(
                #                 row=self.draw_offset.row + 4,
                #                 col=self.draw_offset.col + 1
                #             )
                #         ),
                #         udata=f"{defs.UNIC_SUNNY}"
                #     )
                # )
                # self.sunrise.composite.append(
                #     ansi.ATString(
                #         prefix=ansi.ATStringPrefix(
                #             fgcol=ansi.rainbow.CCTextDefault(),
                #             coords=ansi.ATCoordinates(
                #                 row=self.draw_offset.row + 4,
                #                 col=self.sunrise.composite[0].prefix.coords.col + 2
                #             )
                #         ),
                #         udata=f"{self.weather_data.Variables(APICODE_SUNRISE).Values(0)}"
                #     )
                # )
                # self.sunset.composite.append(
                #     ansi.ATString(
                #         prefix=ansi.ATStringPrefix(
                #             fgcol=ansi.rainbow.CCAppleNPurpleDark(),
                #             coords=ansi.ATCoordinates(
                #                 row=self.draw_offset.row + 4,
                #                 col=self.draw_offset.col + 7
                #             )
                #         ),
                #         udata=f"{defs.UNIC_SUNNY}"
                #     )
                # )
                # self.sunset.composite.append(
                #     ansi.ATString(
                #         prefix=ansi.ATStringPrefix(
                #             fgcol=ansi.rainbow.CCTextDefault(),
                #             coords=ansi.ATCoordinates(
                #                 row=self.draw_offset.row + 4,
                #                 col=self.sunset.composite[0].prefix.coords.col + 2
                #             )
                #         ),
                #         udata=f"{self.weather_data.Variables(APICODE_SUNSET).Values(0)}"
                #     )
                # )

                # # DAYLIGHT/SUNLIGHT DURATION
                # self.daylight_duration.composite.append(
                #     ansi.ATString(
                #         prefix=ansi.ATStringPrefix(
                #             fgcol=ansi.rainbow.CCAppleNYellowLight(),
                #             coords=ansi.ATCoordinates(
                #                 row=self.draw_offset.row + 12,
                #                 col=self.draw_offset.col + 1
                #             )
                #         ),
                #         udata=f"{defs.UNIC_CLOCK}"
                #     )
                # )
                # self.daylight_duration.composite.append(
                #     ansi.ATString(
                #         prefix=ansi.ATStringPrefix(
                #             fgcol=ansi.rainbow.CCTextDefault(),
                #             coords=ansi.ATCoordinates(
                #                 row=self.draw_offset.row + 12,
                #                 col=self.daylight_duration.composite[0].prefix.coords.col + 1
                #             )
                #         ),
                #         udata=f"{self.weather_data.Variables(APICODE_DAYLIGHT_DURATION).Values(0)}"
                #     )
                # )
                # self.sunshine_duration.composite.append(
                #     ansi.ATString(
                #         prefix=ansi.ATStringPrefix(
                #             fgcol=ansi.rainbow.CCAppleNPinkLight(),
                #             coords=ansi.ATCoordinates(
                #                 row=self.draw_offset.row + 12,
                #                 col=self.draw_offset.col + 7
                #             )
                #         ),
                #         udata=f"{defs.UNIC_CLOCK}"
                #     )
                # )
                # self.sunshine_duration.composite.append(
                #     ansi.ATString(
                #         prefix=ansi.ATStringPrefix(
                #             fgcol=ansi.rainbow.CCTextDefault(),
                #             coords=ansi.ATCoordinates(
                #                 row=self.draw_offset.row + 12,
                #                 col=self.sunshine_duration.composite[0].prefix.coords.col + 1
                #             )
                #         )
                #     )
                # )
