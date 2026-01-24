import unittest
from mbpp_835_code import slope

class TestSlope(unittest.TestCase):
    def test_simple_slope(self):
        self.assertAlmostEqual(slope(1, 2, 3, 4), 1.3333333333333333)

    def test_zero_slope(self):
        self.assertEqual(slope(1, 2, 1, 2), 0)

    def test_negative_slope(self):
        self.assertAlmostEqual(slope(3, 4, 1, 2), -0.5)

    def test_vertical_line(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1, 2, 1, 3)

    def test_same_points(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1, 2, 1, 2)

    def test_large_numbers(self):
        self.assertAlmostEqual(slope(1000000000, 2000000000, 3000000000, 4000000000), 1.3333333333333333)
