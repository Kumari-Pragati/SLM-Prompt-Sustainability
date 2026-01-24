import unittest
from mbpp_835_code import slope

class TestSlope(unittest.TestCase):

    def test_positive_slope(self):
        self.assertAlmostEqual(slope(1, 2, 3, 5), 1.6666666666666667)

    def test_zero_slope(self):
        self.assertAlmostEqual(slope(1, 1, 2, 1), 0.0)

    def test_negative_slope(self):
        self.assertAlmostEqual(slope(3, 2, 1, -1), -2.0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError:
            slope(1, 2, 1, 0)

    def test_invalid_input_types(self):
        self.assertRaises(TypeError, slope, 1, 'a', 2, 3)
        self.assertRaises(TypeError, slope, 1, 2, 'a', 3)
