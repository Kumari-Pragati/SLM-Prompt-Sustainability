import unittest
from mbpp_255_code import combinations_colors

class TestCombinationsColors(unittest.TestCase):

    def test_empty_list(self):
        """Test empty list as input"""
        self.assertListEqual(combinations_colors([], 3), [])

    def test_single_element(self):
        """Test single element as input"""
        self.assertListEqual(combinations_colors(["A"], 3), [["A", "A", "A"]])

    def test_multiple_elements(self):
        """Test multiple elements as input"""
        self.assertListEqual(combinations_colors(["A", "B", "C"], 2),
                              [["A", "A"], ["A", "B"], ["A", "C"], ["B", "B"], ["B", "C"], ["C", "C"]])

    def test_large_list(self):
        """Test large list as input"""
        large_list = ["A"] * 100
        self.assertListEqual(combinations_colors(large_list, 10), large_list * len(large_list) // 10)

    def test_negative_n(self):
        """Test negative n as input"""
        with self.assertRaises(ValueError):
            combinations_colors(["A", "B"], -1)

    def test_zero_n(self):
        """Test zero n as input"""
        self.assertListEqual(combinations_colors(["A", "B"], 0), [])
