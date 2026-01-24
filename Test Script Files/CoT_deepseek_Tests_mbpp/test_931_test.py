import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(sum_series(5), 1111.111111111111, places=10)

    def test_zero(self):
        self.assertEqual(sum_series(0), 0)

    def test_negative_number(self):
        with self.assertRaises(ValueError):
            sum_series(-1)

    def test_large_number(self):
        self.assertAlmostEqual(sum_series(100), 338350.0, places=10)
