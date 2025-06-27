"""
Module: distancefunction

Provides a geographic distance calculation function based on the Haversine formula.

This function allows you to compute the great-circle distance between two points
on the Earth, given their latitude and longitude in decimal degrees.

The Earth's mean radius is assumed to be 6371 kilometers.
"""

import math

def distance_lat_long(lat1, lon1, lat2, lon2):
    """
    Calculate the distance between two geographic coordinates using
    the Haversine formula.

    Args:
        lat1 (float): Latitude of the first point in decimal degrees.
        lon1 (float): Longitude of the first point in decimal degrees.
        lat2 (float): Latitude of the second point in decimal degrees.
        lon2 (float): Longitude of the second point in decimal degrees.

    Returns:
        float: Distance in kilometers between the two points.
    """
    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Earth's radius in kilometers
    return 6371.0 * c
import pandas as pd
