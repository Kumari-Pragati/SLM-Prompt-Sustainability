import unittest
from mbpp_931_code import sqrt

def sum_series(number):
    total = 0
    total = pow((number * (number + 1)) / 2, 2)
    return total

class TestSumSeries(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(sum_series(0), 0)

    def test_one(self):
        self.assertEqual(sum_series(1), 1)

    def test_negative_number(self):
        self.assertEqual(sum_series(-1), 1)

    def test_small_number(self):
        self.assertEqual(sum_series(2), 2)

    def test_large_number(self):
        self.assertEqual(round(sum_series(100), 2), round(sqrt(100 * (100 + 1) * (100 + 1) / 4), 2))
