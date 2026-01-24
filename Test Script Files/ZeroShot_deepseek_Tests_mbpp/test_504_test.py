import unittest
from mbpp_504_code import sum_Of_Series

class TestSumOfSeries(unittest.TestCase):

    def test_sum_of_series_positive_numbers(self):
        self.assertEqual(sum_Of_Series(1), 1)
        self.assertEqual(sum_Of_Series(2), 9)
        self.assertEqual(sum_Of_Series(3), 36)
        self.assertEqual(sum_Of_Series(4), 100)

    def test_sum_of_series_zero(self):
        self.assertEqual(sum_Of_Series(0), 0)

    def test_sum_of_series_negative_numbers(self):
        self.assertEqual(sum_Of_Series(-1), 0)
        self.assertEqual(sum_Of_Series(-2), 0)
