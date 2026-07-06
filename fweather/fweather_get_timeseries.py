from shapely.geometry import Point
from shapely.ops import transform
import pyproj


from fweather.fweather_core import get_timeseries_data_cube
from fweather.fweather_data_cube import data_cube
from fweather.fweather_utils import get_all_bands_configs


def get_timeseries(stac_url, collection, start_date, end_date, band, geom):
    """
    Retrieve time series data for a specific band at given geographic locations.
    
    Args:
        stac_url (str): URL endpoint of the STAC API to query.
        collection (str): STAC collection identifier to retrieve data from.
        start_date (str): Start date for temporal filtering in 'YYYY-MM-DD' format.
        end_date (str): End date for temporal filtering in 'YYYY-MM-DD' format.
        band (str): Spectral band identifier for which to retrieve time series data.
        geom (list): List of point geometries as dictionaries with 'coordinates' key,
                     where each dictionary contains coordinates as [longitude, latitude].
    
    Example:
        >>> ts = get_timeseries(
        ...     stac_url=stac_url,
        ...     collection="samet_daily-1",
        ...     start_date="2024-01-01",
        ...     end_date="2024-12-31",
        ...     band="tmean",
        ...     geom=[dict(coordinates=[-11.739, -45.753])],
        ... )
    """
    bands_dict = get_all_bands_configs()
    dataset = bands_dict[collection][band][0]['dataset_name']

    temp_data_cube=data_cube(
        stac_url=stac_url,
        collection=collection,
        start_date=start_date,
        end_date=end_date,
        bbox=get_bbox(geom),
        bands=[band],
        geom=geom
    )
    if (collection == "prec_merge_daily-1"):
        ts=get_timeseries_data_cube(
            datacube=temp_data_cube,
            geom=geom,
            band=dataset
        )
        new_ts = []
        new_tl = []
        for i in range(len(ts['values'])):
            new_ts.append(float(ts['values'][i]))
            new_tl.append(str(ts['timeline'][i])[:19])

        return dict(values=new_ts, timeline=new_tl)
    else:
        timeline = temp_data_cube.coords['time'].values
        ts = []
        tl = []
        for i in range(len(temp_data_cube[dataset].values)):
            ts.append(float(temp_data_cube[dataset].values[i]))
            tl.append(str(timeline[i])[:19])

        return dict(values=ts, timeline=tl)


def get_bbox(geom, radius_meters=2500):

    lat, lon = geom[0]['coordinates'] 
    
    point = Point(lon, lat)
    
    local_crs = f"+proj=aeqd +lat_0={lat} +lon_0={lon} +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs"
    
    project_to_local = pyproj.Transformer.from_proj("EPSG:4326", local_crs, always_xy=True).transform
    project_to_wgs84 = pyproj.Transformer.from_proj(local_crs, "EPSG:4326", always_xy=True).transform
    
    point_local = transform(project_to_local, point)
    buffer_local = point_local.buffer(radius_meters)
    buffer_wgs84 = transform(project_to_wgs84, buffer_local)
    
    min_lon, min_lat, max_lon, max_lat = buffer_wgs84.bounds

    return f"{min_lon}, {min_lat}, {max_lon}, {max_lat}"