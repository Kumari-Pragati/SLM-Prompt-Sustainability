import unittest
from mbpp_835_code import slope

class TestSlope(unittest.TestCase):
    def test_slope_positive(self):
        self.assertAlmostEqual(slope(1, 2, 3, 5), 1.3333333333333333)
        self.assertAlmostEqual(slope(0, 0, 1, 1), 1.0)
        self.assertAlmostEqual(slope(4, 5, 6, 7), 0.6666666666666667)

    def test_slope_zero(self):
        self.assertAlmostEqual(slope(1, 2, 1, 2), 0.0)
        self.assertAlmostEqual(slope(0, 0, 0, 0), 0.0)

    def test_slope_negative(self):
        self.assertAlmostEqual(slope(3, 2, 1, -1), -1.5)
        self.assertAlmostEqual(slope(4, -5, 6, -7), -0.6666666666666667)

    def test_slope_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, slope, 1, 2, 0, 0)
        self.assertRaises(ZeroDivisionError, slope, 0, 0, 1, 0)
