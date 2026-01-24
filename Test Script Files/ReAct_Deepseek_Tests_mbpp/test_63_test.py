import unittest
from mbpp_63_code import max_difference

class TestMaxDifference(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_difference([(1, 2), (3, 4), (5, 6)]), 1)

    def test_negative_numbers(self):
        self.assertEqual(max_difference([(-1, -2), (-3, -4), (-5, -6)]), 1)

    def test_same_numbers(self):
        self.assertEqual(max_difference([(1, 1), (2, 2), (3, 3)]), 0)

    def test_empty_list(self):
        self.assertEqual(max_difference([]), 0)

    def test_single_element(self):
        self.assertEqual(max_difference([(1, 2)]), 1)

    def test_large_numbers(self):
        self.assertEqual(max_difference([(1000000, 2000000), (3000000, 4000000), (5000000, 6000000)]), 1000000)

    def test_float_numbers(self):
        self.assertEqual(max_difference([(1.1, 2.2), (3.3, 4.4), (5.5, 6.6)]), 1.1)

    def test_zero_difference(self):
        self.assertEqual(max_difference([(0, 0), (0, 0), (0, 0)]), 0)
