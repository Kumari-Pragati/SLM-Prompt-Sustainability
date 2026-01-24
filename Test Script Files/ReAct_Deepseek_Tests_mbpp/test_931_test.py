import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(sum_series(5), 1111.0)

    def test_zero_case(self):
        self.assertAlmostEqual(sum_series(0), 0.0)

    def test_negative_case(self):
        with self.assertRaises(ValueError):
            sum_series(-1)

    def test_large_number_case(self):
        self.assertAlmostEqual(sum_series(100), 338350.0)
