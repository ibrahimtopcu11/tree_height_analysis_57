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

def analyze_path_safety(edge_df: pd.DataFrame, path_edges: list) -> float:
    """
    Analyzes the safety of a given path using edge attributes like width, tunnel, bridge, and traffic.

    Parameters:
        edge_df (pd.DataFrame): DataFrame of all edges in the graph.
        path_edges (list): List of tuples (u, v, key) representing the path.

    Returns:
        float: Normalized safety score between 0 (least safe) and 1 (most safe).
    """
    scores = []
    
    for u, v, k in path_edges:
        row = edge_df[(edge_df['u'] == u) & (edge_df['v'] == v) & (edge_df['key'] == k)]
        if row.empty:
            continue
        row = row.iloc[0]
        
        # Basic risk factors
        width = float(row['width']) if pd.notna(row['width']) else 3.0
        tunnel = 1 if str(row['tunnel']).lower() == 'yes' else 0
        bridge = 1 if str(row['bridge']).lower() == 'yes' else 0
        traffic = float(row['traffic_cost']) if 'traffic_cost' in row and pd.notna(row['traffic_cost']) else 0.5

        # Normalize (heuristic)
        width_score = min(width / 10.0, 1.0)
        tunnel_penalty = 0.2 if tunnel else 0
        bridge_penalty = 0.1 if bridge else 0
        traffic_penalty = min(traffic / 10.0, 1.0)

        safety_score = width_score - tunnel_penalty - bridge_penalty - traffic_penalty
        scores.append(max(0.0, min(safety_score, 1.0)))  # Clamp between 0 and 1

    if not scores:
        return 0.0
    
    return sum(scores) / len(scores)
