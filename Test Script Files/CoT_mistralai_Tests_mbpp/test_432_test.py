import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertAlmostEqual(median_trapezium(2, 4, 3), 3.0)
        self.assertAlmostEqual(median_trapezium(5, 3, 4), 4.0)
        self.assertAlmostEqual(median_trapezium(10, 15, 5), 12.5)

    def test_zero_or_negative_numbers(self):
        self.assertAlmostEqual(median_trapezium(0, 0, 5), 0.0)
        self.assertAlmostEqual(median_trapezium(-2, 3, 4), -0.5)
        self.assertAlmostEqual(median_trapezium(0, 0, 0), 0.0)

    def test_one_side_zero(self):
        self.assertAlmostEqual(median_trapezium(0, 5, 3), 2.5)
        self.assertAlmostEqual(median_trapezium(5, 0, 3), 2.5)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, median_trapezium, 'a', 'b', 3)
        self.assertRaises(TypeError, median_trapezium, 1, 2, 'c')
