import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_median_trapezium_positive(self):
        self.assertEqual(median_trapezium(2, 4, 3), 3.0)
        self.assertEqual(median_trapezium(3, 5, 2), 3.5)
        self.assertEqual(median_trapezium(4, 6, 2), 4.5)

    def test_median_trapezium_zero(self):
        self.assertEqual(median_trapezium(0, 0, 0), 0.0)
        self.assertEqual(median_trapezium(0, 2, 0), 1.0)
        self.assertEqual(median_trapezium(2, 0, 0), 1.0)

    def test_median_trapezium_negative(self):
        self.assertEqual(median_trapezium(-2, -4, -3), -3.0)
        self.assertEqual(median_trapezium(-3, -5, -2), -3.5)
        self.assertEqual(median_trapezium(-4, -6, -2), -4.5)
