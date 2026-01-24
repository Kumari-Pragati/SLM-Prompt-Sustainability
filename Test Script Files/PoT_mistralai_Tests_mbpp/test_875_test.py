import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_difference([1, 2, 3, 4]), 1)
        self.assertEqual(min_difference([-1, 0, 1]), 0)
        self.assertEqual(min_difference([5, 2, -3, 4]), 2)

    def test_edge_case_empty_list(self):
        self.assertEqual(min_difference([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(min_difference([0]), 0)

    def test_corner_case_duplicates(self):
        self.assertEqual(min_difference([1, 1, 2]), 0)
        self.assertEqual(min_difference([-1, -1, 0]), 0)
