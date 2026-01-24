import unittest
from mbpp_397_code import median_numbers

class TestMedianNumbers(unittest.TestCase):

    def test_median_with_three_unique_numbers(self):
        self.assertEqual(median_numbers(1, 2, 3), 2)

    def test_median_with_three_equal_numbers(self):
        self.assertEqual(median_numbers(3, 3, 3), 3)

    def test_median_with_two_numbers_and_one_none(self):
        self.assertEqual(median_numbers(1, None), 1)
        self.assertEqual(median_numbers(None, 2), 2)
        self.assertEqual(median_numbers(None, None), None)

    def test_median_with_two_numbers_and_one_zero(self):
        self.assertEqual(median_numbers(1, 0), 1)
        self.assertEqual(median_numbers(0, 2), 2)
        self.assertEqual(median_numbers(0, 0), 0)

    def test_median_with_two_negative_numbers(self):
        self.assertEqual(median_numbers(-1, -2), -1)
        self.assertEqual(median_numbers(-2, -1), -1)

    def test_median_with_two_large_numbers(self):
        self.assertEqual(median_numbers(1000000, 2000000), 1500000)
        self.assertEqual(median_numbers(2000000, 1000000), 1500000)
