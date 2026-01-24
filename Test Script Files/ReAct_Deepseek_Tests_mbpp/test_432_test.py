import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(median_trapezium(10, 20, 5), 15)

    def test_zero_height(self):
        self.assertAlmostEqual(median_trapezium(10, 20, 0), 15)

    def test_equal_bases(self):
        self.assertAlmostEqual(median_trapezium(20, 20, 5), 20)

    def test_negative_bases(self):
        with self.assertRaises(Exception):
            median_trapezium(-10, 20, 5)

    def test_negative_height(self):
        with self.assertRaises(Exception):
            median_trapezium(10, 20, -5)

    def test_zero_bases(self):
        with self.assertRaises(Exception):
            median_trapezium(0, 20, 5)
