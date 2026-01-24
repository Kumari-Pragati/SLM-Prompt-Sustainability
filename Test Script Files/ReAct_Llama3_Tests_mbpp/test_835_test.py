import unittest
from mbpp_835_code import slope

class TestSlope(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(slope(1, 2, 3, 4), 1.0)

    def test_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1, 2, 1, 2)

    def test_vertical_line(self):
        self.assertAlmostEqual(slope(1, 2, 1, 3), float('inf'))

    def test_horizontal_line(self):
        self.assertAlmostEqual(slope(1, 1, 2, 1), 0.0)

    def test_negative_slope(self):
        self.assertAlmostEqual(slope(1, 2, 3, 1), -1.0)

    def test_positive_slope(self):
        self.assertAlmostEqual(slope(1, 1, 3, 2), 1.0)
