import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):

    def test_sum_series_negative(self):
        self.assertEqual(sum_series(-1), 0)

    def test_sum_series_zero(self):
        self.assertEqual(sum_series(0), 0)

    def test_sum_series_one(self):
        self.assertEqual(sum_series(1), 1)

    def test_sum_series_two(self):
        self.assertEqual(sum_series(2), 3)

    def test_sum_series_three(self):
        self.assertEqual(sum_series(3), 6)

    def test_sum_series_four(self):
        self.assertEqual(sum_series(4), 10)

    def test_sum_series_five(self):
        self.assertEqual(sum_series(5), 15)
