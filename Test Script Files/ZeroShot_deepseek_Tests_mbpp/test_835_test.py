import unittest
from mbpp_835_code import slope

class TestSlope(unittest.TestCase):

    def test_slope_positive(self):
        self.assertEqual(slope(1, 2, 3, 4), 1.0)

    def test_slope_negative(self):
        self.assertEqual(slope(1, 2, 3, 0), 0.5)

    def test_slope_zero(self):
        self.assertEqual(slope(1, 2, 1, 2), 0.0)

    def test_slope_infinite(self):
        self.assertEqual(slope(1, 2, 1, 3), float('inf'))

    def test_slope_nan(self):
        self.assertTrue(math.isnan(slope(1, 2, 1, 1)))
