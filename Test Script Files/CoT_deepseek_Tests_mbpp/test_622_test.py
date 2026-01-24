import unittest
from mbpp_622_code import get_median

class TestGetMedian(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(get_median([1, 3, 5], [2, 4, 6], 3), 3.5)

    def test_single_element(self):
        self.assertAlmostEqual(get_median([1], [2], 1), 1.5)

    def test_empty_arrays(self):
        self.assertRaises(IndexError, get_median, [], [], 0)

    def test_large_arrays(self):
        self.assertAlmostEqual(get_median(list(range(1, 10001)), list(range(10001, 20001)), 10000), 10000.5)

    def test_negative_numbers(self):
        self.assertAlmostEqual(get_median([-1, -3, -5], [-2, -4, -6], 3), -3.5)

    def test_duplicate_numbers(self):
        self.assertAlmostEqual(get_median([1, 2, 2], [1, 1, 2], 3), 1.5)
