#
#    This file is part of Python Client Library for FWeather.
#    Copyright (C) 2025 INPE.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.


"""This example shows how to retrieve and plot a time series."""

from fweather import get_timeseries

# Defines URL of a instance of the STAC
stac_url = "https://data.inpe.br/bdc/stac/v1"

# Retrieving the timeseries
ts = get_timeseries(
    stac_url=stac_url,
    collection="samet_daily-1",
    start_date="2024-01-01",
    end_date="2024-12-31",
    band="tmean",
    geom=[dict(coordinates=[-11.739, -45.753])],
)

# Visualizing the timeseries
print(ts)