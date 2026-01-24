import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):
    def test_series_sum(self):
        self.assertEqual(series_sum(1), 1.0)
        self.assertEqual(series_sum(2), 1.5)
        self.assertEqual(series_sum(3), 1.8333333333333333)
        self.assertEqual(series_sum(4), 2.083333333333333)
        self.assertEqual(series_sum(5), 2.25)
