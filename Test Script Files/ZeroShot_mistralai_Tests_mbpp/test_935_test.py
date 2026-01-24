import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):

    def test_series_sum_zero(self):
        self.assertEqual(series_sum(0), 0)

    def test_series_sum_one(self):
        self.assertEqual(series_sum(1), 1)

    def test_series_sum_two(self):
        self.assertEqual(series_sum(2), 9 / 2)

    def test_series_sum_large_number(self):
        self.assertAlmostEqual(series_sum(100), 338350)
