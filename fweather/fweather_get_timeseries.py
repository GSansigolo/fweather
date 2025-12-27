from shapely.geometry import Point
from shapely.ops import transform
import pyproj


from fweather.fweather_core import get_timeseries_data_cube
from fweather.fweather_data_cube import data_cube
from fweather.fweather_utils import get_all_bands_configs


def get_timeseries(stac_url, collection, start_date, end_date, band, geom):
    
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

    timeline = temp_data_cube.coords['time'].values
    ts = []
    for value in temp_data_cube[dataset].values:
        ts.append(float(value))

    return dict(values=ts, timeline=timeline)


def get_bbox(geom, radius_meters=20):

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