import copy

BANDS_CONFIG = {
    "samet_daily-1": {
        "tmean":[
            {'dataset_name': "tmed"}
        ]
    },
    "prec_merge_daily-1": {
        "merge_daily":[
            {'dataset_name': "rdp"}
        ]
    },
}

def get_all_bands_configs():
    """
    Get all cloud configurations.
    
    Returns:
        Dictionary of all cloud configurations
    """
    return copy.deepcopy(BANDS_CONFIG)

