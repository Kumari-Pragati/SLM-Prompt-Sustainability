import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(sum_series(5), 62.5)

    def test_zero(self):
        self.assertEqual(sum_series(0), 0)

    def test_negative_integer(self):
        self.assertEqual(sum_series(-3), 18.75)

    def test_fraction(self):
        self.assertAlmostEqual(sum_series(1.5), 1.5625)

    def test_non_integer(self):
        self.assertRaises(TypeError, sum_series, 'not_an_integer')
