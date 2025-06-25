# Tree Height Analysis

This Python package analyzes tree height data from `.txt` files and calculates:

- The minimum and maximum tree heights
- Tree types with extreme heights
- Geodesic distance between them using Haversine formula.

## Example usage

```python
from tree_height_analysis.analyzer import parse_tree_data, analyze_tree_heights

trees = parse_tree_data("sample_dataset/trees_complex.txt")
results = analyze_tree_heights(trees)
print(results)
