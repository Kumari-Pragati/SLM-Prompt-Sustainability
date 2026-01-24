import unittest
from mbpp_931_code import sum_series

class TestSumSeries(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(sum_series(1), 1)
        self.assertEqual(sum_series(2), 2)
        self.assertEqual(sum_series(10), 285)

    def test_zero(self):
        self.assertEqual(sum_series(0), 0)

    def test_negative_integer(self):
        self.assertEqual(sum_series(-1), 1)
        self.assertEqual(sum_series(-2), 2)
        self.assertEqual(sum_series(-10), 285)

    def test_floating_point(self):
        self.assertAlmostEqual(sum_series(3.5), 14.125, delta=0.01)

    def test_non_integer(self):
        self.assertRaises(TypeError, sum_series, "string")
        self.assertRaises(TypeError, sum_series, 3.14)
