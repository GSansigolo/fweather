import xarray as xr

def save_xarray(ds, filename):
    """
    Save an xarray dataset or data array to a NetCDF file.
    
    Args:
        ds (xarray.Dataset or xarray.DataArray): The xarray object to save to file.
        filename (str): Path for the output NetCDF file where the data will be saved.
    """
    if isinstance(ds, xr.DataArray):
        ds = ds.to_dataset(name='dataarray')
        ds.attrs['_xarray_type'] = 'DataArray'
    ds.to_netcdf(filename)
    print(f"xarray object saved to {filename}")