import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(2), 3)
        self.assertEqual(sum_series(3), 5)
        self.assertEqual(sum_series(4), 9)
        self.assertEqual(sum_series(5), 13)

    def test_zero(self):
        self.assertEqual(sum_series(0), 0)

    def test_negative_numbers(self):
        self.assertEqual(sum_series(-1), 1)
        self.assertEqual(sum_series(-2), -1)
        self.assertEqual(sum_series(-3), 1)

    def test_large_numbers(self):
        self.assertEqual(sum_series(100), 9901)

    def test_small_numbers(self):
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(2), 3)
        self.assertEqual(sum_series(3), 5)
