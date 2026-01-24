import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):

    def test_max_difference_positive_numbers(self):
        self.assertEqual(max_difference([(1, 2), (3, 4), (5, 6)]), 5)

    def test_max_difference_negative_numbers(self):
        self.assertEqual(max_difference([(-1, -2), (-3, -4), (-5, -6)]), 5)

    def test_max_difference_mixed_numbers(self):
        self.assertEqual(max_difference([(-1, 2), (3, -4), (5, 6)]), 11)

    def test_max_difference_single_number(self):
        self.assertEqual(max_difference([(1, 1)]), 0)

    def test_max_difference_empty_list(self):
        self.assertEqual(max_difference([]), 0)
