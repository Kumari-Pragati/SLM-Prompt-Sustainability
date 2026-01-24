import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertAlmostEqual(median_trapezium(2, 3, 1), 2.5)

    def test_zero_base(self):
        self.assertAlmostEqual(median_trapezium(0, 4, 2), 2.0)

    def test_negative_base(self):
        self.assertAlmostEqual(median_trapezium(-2, -3, 1), -1.5)

    def test_zero_height(self):
        self.assertAlmostEqual(median_trapezium(2, 3, 0), 2.0)

    def test_negative_numbers(self):
        self.assertAlmostEqual(median_trapezium(-2, -3, -1), 0.5)
