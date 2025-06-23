import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from tree_height_analysis_57.analyzer import parse_tree_data, analyze_tree_heights
def test_analysis():
    trees = parse_tree_data("sample_dataset/trees_complex.txt")
    result = analyze_tree_heights(trees)
    assert result["min"]["height"] < result["max"]["height"]
    assert result["distance"] > 0
