#!/usr/bin/env python3
"""
WeatherTable Module

Adding my own whacked out table implementation.

Bcuz.
"""

import weather_day_view as wdv
import ansi

class WeatherTableCell:
    WIDTH             = 14
    HEIGHT            = 4
    BORDER_HORIZONTAL = '-'
    BORDER_VERTICAL   = '|'

    def __init__(self, **kwargs) -> None:
        self.use_border   = kwargs['use_border'] if 'use_border' in kwargs else True
        self.weather_data = kwargs['weather_data'] if 'weather_data' in kwargs else None
        self.origin_point = kwargs['origin_point'] if 'origin_point' in kwargs else ansi.ATCoordinatesNone()
        self.table_pos    = kwargs['table_pos'] if 'table_pos' in kwargs else 0

        self.weather_view = wdv.WeatherDayView(
            weather_data = self.weather_data,
            day_offset   = self.table_pos,
            draw_offset  = self.origin_point
        )

    def __str__(self) -> str:
        a = ''

        if self.use_border:
            # I'M A DUMBASS
            # THIS FAILS ON THE SECOND CELL BECAUSE BY THIS POINT,
            # ORIGIN_POINT.COL IS GREATER THAN WEATHERTABLECELL.WIDTH
            # WHICH EXPLAINS WHY YOU DON'T EVEN SEE THE ANSI DATA
            # IN THE STRING.
            for b in range(self.origin_point.col, (self.origin_point.col + WeatherTableCell.WIDTH)):
                a += ansi.ATString(
                    prefix=ansi.ATStringPrefix(
                        fgcol=ansi.rainbow.CCTextDefault(),
                        coords=ansi.ATCoordinates(
                            row=self.origin_point.row,
                            col=b
                        )
                    ),
                    udata=f"{WeatherTableCell.BORDER_HORIZONTAL}"
                ).to_ansi_str()
                a += ansi.ATString(
                    prefix=ansi.ATStringPrefix(
                        fgcol=ansi.rainbow.CCTextDefault(),
                        coords=ansi.ATCoordinates(
                            row=self.origin_point.row + WeatherTableCell.HEIGHT,
                            col=b
                        )
                    ),
                    udata=f"{WeatherTableCell.BORDER_HORIZONTAL}"
                ).to_ansi_str()
            for c in range(self.origin_point.row, WeatherTableCell.HEIGHT):
                a += ansi.ATString(
                    prefix=ansi.ATStringPrefix(
                        fgcol=ansi.rainbow.CCTextDefault(),
                        coords=ansi.ATCoordinates(
                            row=self.origin_point.row + c,
                            col=self.origin_point.col
                        )
                    ),
                    udata=f"{WeatherTableCell.BORDER_VERTICAL}"
                ).to_ansi_str()
                a += ansi.ATString(
                    prefix=ansi.ATStringPrefix(
                        fgcol=ansi.rainbow.CCTextDefault(),
                        coords=ansi.ATCoordinates(
                            row=self.origin_point.row + c,
                            col=self.origin_point.col + WeatherTableCell.WIDTH
                        )
                    ),
                    udata=f"{WeatherTableCell.BORDER_VERTICAL}"
                ).to_ansi_str()

        # THIS MAY NOT WORK, BUT FUCK IT
        a += self.weather_view.__str__()

        return a


class WeatherTable:
    def __init__(self, **kwargs) -> None:
        self.width        = kwargs['width'] if 'width' in kwargs else 7
        self.weather_data = kwargs['weather_data'] if 'weather_data' in kwargs else None

        self.cells = []

        self.create_cell_table()

    def create_cell_table(self):
        for a in range(0, self.width):
            self.cells.append(
                WeatherTableCell(
                    weather_data=self.weather_data,
                    origin_point=ansi.ATCoordinates(
                        row=1,
                        col=(a * WeatherTableCell.WIDTH)
                    ),
                    table_pos=a
                )
            )

    def __str__(self) -> str:
        a = ''

        for b in range(0, len(self.cells)):
            a += self.cells[b].__str__()

        return a
