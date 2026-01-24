import unittest
from mbpp_835_code import slope

class TestSlopeFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(slope(1, 2, 4, 8), 2.0)

    def test_negative_slope(self):
        self.assertAlmostEqual(slope(4, 8, 1, 2), -2.0)

    def test_vertical_line(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1, 2, 1, 3)

    def test_same_points(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1, 2, 1, 2)

    def test_zero_slope(self):
        self.assertEqual(slope(1, 0, 2, 0), 0.0)

    def test_large_numbers(self):
        self.assertAlmostEqual(slope(1000000, 2000000, 4000000, 8000000), 0.5)

    def test_float_inputs(self):
        self.assertAlmostEqual(slope(1.5, 2.5, 4.5, 8.5), 1.0)
