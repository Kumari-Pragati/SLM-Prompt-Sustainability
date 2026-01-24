import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_sum_series_with_positive_numbers(self):
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(3), 6)
        self.assertEqual(sum_series(5), 10)

    def test_sum_series_with_negative_numbers(self):
        self.assertEqual(sum_series(-1), 0)
        self.assertEqual(sum_series(-3), 0)

    def test_sum_series_with_zero(self):
        self.assertEqual(sum_series(0), 0)
