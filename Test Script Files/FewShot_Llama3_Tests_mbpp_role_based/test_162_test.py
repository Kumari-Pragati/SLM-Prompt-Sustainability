import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):
    def test_sum_series_zero(self):
        self.assertEqual(sum_series(0), 0)

    def test_sum_series_positive(self):
        self.assertEqual(sum_series(5), 15)

    def test_sum_series_negative(self):
        self.assertEqual(sum_series(-3), 0)

    def test_sum_series_large(self):
        self.assertEqual(sum_series(10), 55)

    def test_sum_series_invalid_type(self):
        with self.assertRaises(TypeError):
            sum_series("a")
