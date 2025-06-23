"""
Module: analyzer

This module provides core functions to read and analyze tree height data
from a tab-separated text file. It includes functionality to:

- Parse a dataset containing tree ID, coordinates, type, and height
- Identify trees with minimum and maximum height
- Compute the geographical distance between them using the Haversine formula
"""

from .distancefunction import distance_lat_long


def parse_tree_data(file_path):
    """
    Parse tree data from a tab-separated text file.

    Each row in the file is expected to contain:
    ID, Latitude, Longitude, Tree Type, and Height.

    Args:
        file_path (str): Path to the input .txt dataset file.

    Returns:
        dict: A dictionary with the following structure:
            {
                "id": {tree_id: str, ...},
                "lat": {tree_id: float, ...},
                "lon": {tree_id: float, ...},
                "type": {tree_id: str, ...},
                "height": {tree_id: float, ...}
            }
    """
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]
    header = lines[0].split('\t')
    data = [line.split('\t') for line in lines[1:]]

    trees = {
        "id": {}, "lat": {}, "lon": {}, "type": {}, "height": {}
    }

    for row in data:
        tid = row[0]
        trees["id"][tid] = tid
        trees["lat"][tid] = float(row[1])
        trees["lon"][tid] = float(row[2])
        trees["type"][tid] = row[3]
        trees["height"][tid] = float(row[4])
    
    return trees


def analyze_tree_heights(trees):
    """
    Analyze the tree dataset to find the minimum and maximum height trees,
    along with their types, coordinates, and the distance between them.

    Args:
        trees (dict): Parsed tree data dictionary as returned by `parse_tree_data`.

    Returns:
        dict: A dictionary with the structure:
            {
                "min": {
                    "id": str,
                    "type": str,
                    "height": float,
                    "lat": float,
                    "lon": float
                },
                "max": {
                    "id": str,
                    "type": str,
                    "height": float,
                    "lat": float,
                    "lon": float
                },
                "distance": float  # in kilometers
            }
    """
    min_id = min(trees["height"], key=trees["height"].get)
    max_id = max(trees["height"], key=trees["height"].get)
    
    result = {
        "min": {
            "id": min_id,
            "type": trees["type"][min_id],
            "height": trees["height"][min_id],
            "lat": trees["lat"][min_id],
            "lon": trees["lon"][min_id]
        },
        "max": {
            "id": max_id,
            "type": trees["type"][max_id],
            "height": trees["height"][max_id],
            "lat": trees["lat"][max_id],
            "lon": trees["lon"][max_id]
        },
        "distance": distance_lat_long(
            trees["lat"][min_id], trees["lon"][min_id],
            trees["lat"][max_id], trees["lon"][max_id]
        )
    }
    return result
