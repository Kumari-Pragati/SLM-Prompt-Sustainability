import unittest
from mbpp_181_code import common_prefix

class TestCommonPrefix(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(common_prefix([ "flower", "flow", "flight" ], 3), "fl")
        self.assertEqual(common_prefix([ "dog", "racecar", "car" ], 3), "")
        self.assertEqual(common_prefix([ "apple", "apples", "apricot" ], 3), "app")

    def test_edge_case_empty_list(self):
        self.assertIsNone(common_prefix([], 0))

    def test_edge_case_single_item(self):
        self.assertEqual(common_prefix([ "abc" ], 1), "abc")

    def test_edge_case_single_item_empty_string(self):
        self.assertEqual(common_prefix([ "" ], 1), "")

    def test_edge_case_different_lengths(self):
        self.assertEqual(common_prefix([ "flower", "flowerz" ], 2), "fl")
        self.assertEqual(common_prefix([ "flower", "flowerz", "flowerzz" ], 3), "fl")

    def test_corner_case_all_empty_strings(self):
        self.assertEqual(common_prefix([ "", "", "" ], 3), "")

    def test_corner_case_all_same_strings(self):
        self.assertEqual(common_prefix([ "flower", "flower", "flower" ], 3), "flower")
