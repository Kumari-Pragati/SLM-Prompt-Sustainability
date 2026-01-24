import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(series_sum(1), 1 / 6)
        self.assertEqual(series_sum(2), 9 / 20)
        self.assertEqual(series_sum(10), 285 / 288)

    def test_zero(self):
        self.assertEqual(series_sum(0), 0)

    def test_negative_integer(self):
        self.assertEqual(series_sum(-1), -1 / 6)
        self.assertEqual(series_sum(-2), -21 / 20)
        self.assertEqual(series_sum(-10), -285 / 288)
