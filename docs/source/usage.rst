Usage
=====

To use the package:

.. code-block:: python

    from tree_height_analysis.analyzer import parse_tree_data, analyze_tree_heights

    trees = parse_tree_data("sample_dataset/trees_complex.txt")
    results = analyze_tree_heights(trees)
    print(results)