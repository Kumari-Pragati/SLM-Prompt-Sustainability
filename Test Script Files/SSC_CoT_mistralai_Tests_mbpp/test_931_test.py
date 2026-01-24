import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(sum_series(5), 56.25)

    def test_edge_cases(self):
        self.assertEqual(sum_series(0), 0)
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(2), 9)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            sum_series(-1)

    def test_fractional_input(self):
        with self.assertRaises(ValueError):
            sum_series(3.5)

    def test_large_input(self):
        with self.assertRaises(OverflowError):
            sum_series(1000000)
