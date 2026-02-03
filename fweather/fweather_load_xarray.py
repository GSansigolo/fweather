import xarray as xr

def load_xarray(filename, decode_times=False):
    """
    Load an xarray dataset or data array from a file, with optional time decoding.
    
    Args:
        filename (str): Path to the input file to load.
        decode_times (bool, optional): Whether to decode time variables in the dataset.
            Set to False for performance when time decoding is not needed. Defaults to False.
    
    Returns:
        xarray.Dataset: Loaded xarray object. Returns a DataArray if the file
        was originally saved as a DataArray with the '_xarray_type' attribute, otherwise returns a Dataset.
    """
    ds = xr.open_dataset(filename, decode_times=decode_times)
    if '_xarray_type' in ds.attrs and ds.attrs['_xarray_type'] == 'DataArray':
        da = ds['dataarray']
        da.attrs = {k: v for k, v in ds.attrs.items() if k != '_xarray_type'}
        ds.close()
        return da
    else:
        return ds
    