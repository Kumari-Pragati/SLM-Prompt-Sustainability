import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(median_trapezium(10, 20, 5), 15)

    def test_zero_height(self):
        self.assertAlmostEqual(median_trapezium(10, 20, 0), 15)

    def test_negative_heights(self):
        self.assertAlmostEqual(median_trapezium(10, 20, -5), 7.5)

    def test_equal_bases(self):
        self.assertAlmostEqual(median_trapezium(20, 20, 5), 20)

    def test_zero_bases(self):
        self.assertAlmostEqual(median_trapezium(0, 0, 5), 0)

    def test_negative_bases(self):
        self.assertAlmostEqual(median_trapezium(-10, -20, 5), -15)

    def test_negative_and_positive_bases(self):
        self.assertAlmostEqual(median_trapezium(-10, 20, 5), 5)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            median_trapezium("10", 20, 5)

    def test_invalid_input_value(self):
        with self.assertRaises(ValueError):
            median_trapezium(10, 20, 100)
