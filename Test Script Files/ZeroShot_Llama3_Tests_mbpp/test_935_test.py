import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):

    def test_series_sum_positive(self):
        self.assertEqual(series_sum(1), 1)
        self.assertEqual(series_sum(2), 3)
        self.assertEqual(series_sum(3), 6)
        self.assertEqual(series_sum(4), 10)
        self.assertEqual(series_sum(5), 15)

    def test_series_sum_negative(self):
        with self.assertRaises(TypeError):
            series_sum(-1)

    def test_series_sum_zero(self):
        self.assertEqual(series_sum(0), 0)

    def test_series_sum_non_integer(self):
        with self.assertRaises(TypeError):
            series_sum(1.5)
