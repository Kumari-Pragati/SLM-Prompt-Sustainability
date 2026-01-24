import unittest
from mbpp_875_code import min_difference

class TestMinDifference(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(min_difference([(1, 2), (3, 4), (5, 6)]), 1)

    def test_negative_numbers(self):
        self.assertEqual(min_difference([(-1, -2), (-3, -4), (-5, -6)]), 1)

    def test_single_element(self):
        self.assertEqual(min_difference([(1,)]), 0)

    def test_empty_list(self):
        self.assertEqual(min_difference([]), None)

    def test_mixed_numbers(self):
        self.assertEqual(min_difference([(1, -2), (-3, 4), (5, -6)]), 1)
