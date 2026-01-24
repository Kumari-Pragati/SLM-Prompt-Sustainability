import unittest
from mbpp_935_code import series_sum

class TestSeriesSum(unittest.TestCase):

    def test_positive_integer(self):
        self.assertEqual(series_sum(1), 1)
        self.assertEqual(series_sum(2), 9/2)
        self.assertEqual(series_sum(5), 1215/60)

    def test_zero(self):
        self.assertEqual(series_sum(0), 0)

    def test_negative_integer(self):
        self.assertEqual(series_sum(-1), -1/6)
        self.assertEqual(series_sum(-2), -17/6)
        self.assertEqual(series_sum(-5), -1215/60)

    def test_floats(self):
        self.assertAlmostEqual(series_sum(3.5), 1231.5/60)
        self.assertAlmostEqual(series_sum(4.2), 1392.4/60)

    def test_large_integer(self):
        self.assertEqual(series_sum(100), 335503350/60)

    def test_invalid_input(self):
        self.assertRaises(TypeError, series_sum, 'string')
        self.assertRaises(TypeError, series_sum, 0.5 + 2j)
