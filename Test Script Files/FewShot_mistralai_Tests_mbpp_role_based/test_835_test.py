import unittest
from mbpp_835_code import slope

class TestSlope(unittest.TestCase):
    def test_positive_slope(self):
        self.assertAlmostEqual(slope(1, 2, 3, 5), 1.6666666666666667)

    def test_zero_slope(self):
        self.assertAlmostEqual(slope(1, 1, 1, 1), 0.0)

    def test_negative_slope(self):
        self.assertAlmostEqual(slope(1, 2, 3, -1), -0.6666666666666667)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            slope(0, 0, 0, 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            slope('a', 'b', 'c', 'd')
