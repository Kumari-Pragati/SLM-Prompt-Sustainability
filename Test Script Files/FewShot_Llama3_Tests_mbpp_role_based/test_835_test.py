import unittest
from mbpp_835_code import slope

class TestSlope(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertAlmostEqual(slope(1, 2, 3, 4), 1.0)

    def test_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            slope(1, 2, 1, 2)

    def test_negative_numbers(self):
        self.assertAlmostEqual(slope(-1, -2, -3, -4), 1.0)

    def test_zero_slope(self):
        self.assertAlmostEqual(slope(1, 1, 2, 1), 0.0)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            slope('a', 'b', 'c', 'd')

    def test_invalid_input_value(self):
        with self.assertRaises(TypeError):
            slope(1, 'b', 2, 3)
