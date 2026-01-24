import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(series_sum(1), 1)
        self.assertEqual(series_sum(2), 9 / 2)
        self.assertEqual(series_sum(5), 101)

    def test_edge_cases(self):
        self.assertEqual(series_sum(0), 0)
        self.assertEqual(series_sum(100), 199500)

    def test_negative_input(self):
        self.assertRaises(ValueError, series_sum, -1)

    def test_fractional_input(self):
        self.assertRaises(TypeError, series_sum, 3.14)
