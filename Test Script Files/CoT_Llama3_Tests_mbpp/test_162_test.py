import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_sum_series_zero(self):
        self.assertEqual(sum_series(0), 0)

    def test_sum_series_negative(self):
        self.assertEqual(sum_series(-1), 0)

    def test_sum_series_positive(self):
        self.assertEqual(sum_series(1), 1)

    def test_sum_series_recursive(self):
        self.assertEqual(sum_series(3), 5)

    def test_sum_series_recursive_large(self):
        self.assertEqual(sum_series(10), 30)

    def test_sum_series_recursive_invalid(self):
        with self.assertRaises(RecursionError):
            sum_series(10000)
