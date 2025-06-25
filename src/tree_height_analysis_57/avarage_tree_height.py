def average_tree_height(trees: dict) -> float:
    """
    Calculate the average height of all trees in the dataset.

    Parameters
    ----------
    trees : dict
        A dictionary returned by `parse_tree_data` that contains tree heights under the "height" key.

    Returns
    -------
    float
        The average tree height in meters.
    
    Example
    -------
    >>> trees = parse_tree_data("sample_dataset/trees_complex.txt")
    >>> avg = average_tree_height(trees)
    >>> print(avg)
    12.53
    """
    heights = list(trees["height"].values())
    if not heights:
        return 0.0
    return sum(heights) / len(heights)
def filter_tall_trees(trees, min_height):
    """
    Filter and return trees that are taller than a given minimum height.

    Parameters:
        trees (dict): Dictionary of tree data, where each value includes a 'height' field.
        min_height (float): The minimum height threshold in meters.

    Returns:
        dict: A dictionary containing only the trees taller than the given threshold.
    
    Example:
        >>> trees = {
        ...     "T001": {"height": 12.5},
        ...     "T002": {"height": 18.2},
        ...     "T003": {"height": 9.1}
        ... }
        >>> filter_tall_trees(trees, 10.0)
        {'T001': {'height': 12.5}, 'T002': {'height': 18.2}}
    """
    return {tid: info for tid, info in trees.items() if info["height"] > min_height}
