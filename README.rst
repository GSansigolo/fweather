..
    This file is part of fweather - Python package for meteorological time series analysis.
    Copyright (C) 2026 INPE.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/gpl-3.0.html>.

.. image:: https://raw.githubusercontent.com/GSansigolo/fweather/main/docs/img/fweather.png
   :width: 300
   :align: center
   :alt: fweather logo

=================================================================
fweather - Python package for meteorological time series analysis
=================================================================


.. image:: https://img.shields.io/badge/License-GPLv3-blue.svg
        :target: https://github.com/GSansigolo/fweather/blob/master/LICENSE
        :alt: Software License


.. image:: https://readthedocs.org/projects/fweather/badge/?version=latest
        :target: https://fweather.readthedocs.io/en/latest/
        :alt: Documentation Status


.. image:: https://img.shields.io/badge/lifecycle-stable-green.svg
        :target: https://www.tidyverse.org/lifecycle/#stable
        :alt: Software Life Cycle


.. image:: https://img.shields.io/github/tag/GSansigolo/fweather.svg
        :target: https://github.com/GSansigolo/fweather/releases
        :alt: Release


.. image:: https://img.shields.io/pypi/v/fweather
        :target: https://pypi.org/project/fweather/
        :alt: Python Package Index


.. image:: https://img.shields.io/discord/689541907621085198?logo=discord&logoColor=ffffff&color=7389D8
        :target: https://discord.com/channels/689541907621085198#
        :alt: Join us at Discord


About
=====

The development of software to manipulate meteorological data has always been challenging, this difficulties scale with the growing volume of satellite images currently available. To overcome the challenges, we need to develop tools that can process data sets using the advantages of a server-side infrastructure. 

In order to perform large-scale agriculture monitoring, we need to have dedicated packages that target the peculiarities of the large-scale data analysis. Meteorological data packages have been modeled for a specific type of operation, typically targeting analysts with programming background, and they in most part are not prepared to deal with big data. 

This repository contains fweather, a free and open-source Python package for meteorological time series analysis. It used the SpatioTemporal Asset Catalog (STAC) to access meteorological data and retrieve it as virtual data cubes, facilitating the retrieval of time series. It provides methods of building a virtual data cube and retrieving time series of cumulative precipitation, daily precipitation, temperature and climate change projections. With the package, it’s possible to perform large-scale agriculture monitoring using meteorological time series with no need to download data locally and programming skills.

The fweather package has a group of functions, some of which are: 

- ``data_cube``: create multi-dimensional arrays from weather and climate data.

- ``get_timeseries``: return a weather and climate time series.

- ``get_timeseries_data_cube``: return a weather and climate time series from a ``data_cube``.

Installation
============

See `INSTALL.rst <https://github.com/GSansigolo/fweather/blob/master/INSTALL.rst>`_.


Documentation
=============

See https://fweather.readthedocs.io/en/latest.


References
==========


WIP


License
=======


.. admonition::
    Copyright (C) 2026 INPE.

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
