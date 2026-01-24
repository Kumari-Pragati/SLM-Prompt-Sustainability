import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_median_trapezium(self):
        self.assertEqual(median_trapezium(10, 20, 5), 15)
        self.assertEqual(median_trapezium(15, 15, 10), 15)
        self.assertEqual(median_trapezium(2, 3, 4), 2.5)
        self.assertEqual(median_trapezium(0, 0, 0), 0)
        self.assertEqual(median_trapezium(-1, -2, -3), -1.5)
