import unittest
from mbpp_835_code import slope

class TestSlopeFunction(unittest.TestCase):

    def test_slope_positive(self):
        self.assertAlmostEqual(slope(1,2,3,4), 0.6666666666666666)

    def test_slope_negative(self):
        self.assertAlmostEqual(slope(1,2,3,1), -1.0)

    def test_slope_zero(self):
        self.assertAlmostEqual(slope(1,1,1,1), 0.0)

    def test_slope_zero_x(self):
        self.assertAlmostEqual(slope(1,2,1,2), float('inf'))

    def test_slope_zero_y(self):
        self.assertAlmostEqual(slope(1,2,2,2), 0.0)

    def test_slope_zero_x_y(self):
        self.assertAlmostEqual(slope(1,1,1,1), float('inf'))

    def test_slope_zero_x_y_negative(self):
        self.assertAlmostEqual(slope(1,1,1,2), -float('inf'))

    def test_slope_zero_x_y_positive(self):
        self.assertAlmostEqual(slope(1,1,2,1), float('inf'))
