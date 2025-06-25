Usage
=====

This guide shows how to use the ``tree_height_analysis_57`` package to load tree data,
analyze heights, and compute the distance between the tallest and shortest trees.

.. contents::
   :local:
   :depth: 2
   :class: this-will-duplicate-information-and-it-is-still-useful-here

Getting Started
---------------

To begin using the package, make sure your dataset is a tab-separated `.txt` file
with the following columns:

::

    id    latitude    longitude    type    height

For example:

::

    T001    39.9208    32.8541    Oak    12.5

You can use the main functions by importing them as follows:

.. code-block:: python

    from tree_height_analysis_57.analyzer import parse_tree_data, analyze_tree_heights

    # Load data from your text file
    trees = parse_tree_data("sample_dataset/trees_complex.txt")

    # Analyze tree height data
    results = analyze_tree_heights(trees)

    # Print results
    print("Minimum Height Tree:", results["min"])
    print("Maximum Height Tree:", results["max"])
    print("Distance Between Min and Max (km):", results["distance"])


Function Overview
-----------------

**`parse_tree_data(file_path)`**

- Loads tree data from a `.txt` file.
- Returns a dictionary containing all tree attributes by ID.

**`analyze_tree_heights(trees)`**

- Finds the tree with the shortest and tallest height.
- Returns both trees and their geographic distance.

This function internally uses:

**`distance_lat_long(lat1, lon1, lat2, lon2)`**

- Located in `distancefunction.py`
- Calculates geographic distance using the Haversine formula.


Additional Notes
----------------

- You can place your dataset in any folder, just update the path.
- If you're building documentation, make sure this usage example is included in the `index.rst` to appear on Read the Docs.
