import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_sum_series(self):
        self.assertAlmostEqual(sum_series(1), 1.0)
        self.assertAlmostEqual(sum_series(2), 14.0)
        self.assertAlmostEqual(sum_series(3), 144.0)
        self.assertAlmostEqual(sum_series(4), 1156.0)
        self.assertAlmostEqual(sum_series(5), 8644.0)
