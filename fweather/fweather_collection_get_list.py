from tqdm import tqdm

def collection_get_list(stac, datacube):
    """
    Query a STAC catalog and retrieve asset URLs for specified bands within a spatiotemporal extent.
    
    Args:
        stac (object): An initialized STAC client connection to the catalog API.
        datacube (dict): Dictionary containing query parameters with the following keys:
            collection (str): STAC collection identifier to search within.
            bbox (list/tuple): Bounding box coordinates [minx, miny, maxx, maxy] for spatial filtering.
            start_date (str): Start date for temporal filtering in 'YYYY-MM-DD' format.
            end_date (str): End date for temporal filtering in 'YYYY-MM-DD' format.
            bands (list): List of band identifiers to retrieve asset URLs for.
    
    Returns:
        dict: A dictionary where each key is a band identifier and the value is a list 
              of asset URLs (hrefs) for that band across all matching scenes.
    """
    collection = datacube['collection']
    bbox = datacube['bbox']
    start_date = datacube['start_date']
    end_date = datacube['end_date']
    bands = datacube['bands'] 

    if (datacube['bbox']):
        item_search = stac.search(
            collections=[collection],
            datetime=f"{start_date}T00:00:00Z/{end_date}T00:00:00Z",
            bbox=bbox
        )

    band_dict = {}
    for band in bands:
        band_dict[band] = []

    for item in item_search.items():
        for band in bands:
            asset = item.assets.get(band)
            if asset and hasattr(asset, 'href'):
                band_dict[band].append(asset.href)

    return band_dict