import unittest
from mbpp_835_code import slope

class TestSlope(unittest.TestCase):

    def test_slope_with_positive_x_and_y(self):
        self.assertAlmostEqual(slope(1, 2, 3, 4), 0.66666667)

    def test_slope_with_zero_x(self):
        with self.assertRaises(ZeroDivisionError):
            slope(0, 2, 3, 4)

    def test_slope_with_negative_x_and_y(self):
        self.assertAlmostEqual(slope(-1, -2, -3, -4), 0.66666667)

    def test_slope_with_same_x_and_y(self):
        self.assertAlmostEqual(slope(1, 2, 1, 2), 0)

    def test_slope_with_vertical_line(self):
        self.assertAlmostEqual(slope(1, 2, 1, 3), float('nan'))

    def test_slope_with_horizontal_line(self):
        self.assertAlmostEqual(slope(1, 2, 2, 2), 0)
