import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_positive_numbers(self):
        """Test median calculation with positive numbers"""
        self.assertEqual(median_trapezium(3, 4, 1), 2.5)
        self.assertEqual(median_trapezium(5, 6, 2), 5.5)
        self.assertEqual(median_trapezium(10, 20, 5), 12.5)

    def test_zero_or_negative_numbers(self):
        """Test median calculation with zero or negative numbers"""
        self.assertAlmostEqual(median_trapezium(0, 0, 1), 0.0, delta=0.01)
        self.assertAlmostEqual(median_trapezium(-3, 0, 1), -1.5, delta=0.01)
        self.assertAlmostEqual(median_trapezium(0, -3, 1), -1.5, delta=0.01)
        self.assertRaises(ValueError, median_trapezium, 0, 0, 0)
        self.assertRaises(ValueError, median_trapezium, -3, -3, 0)
        self.assertRaises(ValueError, median_trapezium, 3, -3, 0)

    def test_zero_base(self):
        """Test median calculation with one base as zero"""
        self.assertAlmostEqual(median_trapezium(0, 3, 1), 1.5, delta=0.01)
        self.assertAlmostEqual(median_trapezium(3, 0, 1), 1.5, delta=0.01)

    def test_zero_height(self):
        """Test median calculation with zero height"""
        self.assertEqual(median_trapezium(3, 4, 0), 3.0)
        self.assertEqual(median_trapezium(4, 3, 0), 3.0)
