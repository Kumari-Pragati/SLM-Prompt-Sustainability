import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_median_trapezium(self):
        self.assertEqual(median_trapezium(5, 5, 10), 5.0)
        self.assertEqual(median_trapezium(10, 5, 10), 5.0)
        self.assertEqual(median_trapezium(5, 10, 10), 5.0)
        self.assertEqual(median_trapezium(10, 10, 10), 10.0)
        self.assertEqual(median_trapezium(5, 5, 5), 5.0)
        self.assertEqual(median_trapezium(10, 10, 5), 5.0)
        self.assertEqual(median_trapezium(5, 10, 5), 5.0)
        self.assertEqual(median_trapezium(10, 5, 5), 5.0)
