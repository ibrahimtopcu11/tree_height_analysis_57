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
