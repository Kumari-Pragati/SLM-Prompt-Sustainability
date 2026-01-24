import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(median_trapezium(1, 2, 3), 2.0)
        self.assertEqual(median_trapezium(2, 2, 1), 2.0)
        self.assertEqual(median_trapezium(3, 4, 5), 4.0)

    def test_edge_and_boundary(self):
        self.assertEqual(median_trapezium(0, 1, 2), 0.5)
        self.assertEqual(median_trapezium(1, 0, 2), 0.5)
        self.assertEqual(median_trapezium(1, 1, 0), 1.0)
        self.assertEqual(median_trapezium(1, 1, 1), 1.0)
        self.assertEqual(median_trapezium(float('inf'), 1, 2), float('inf'))
        self.assertEqual(median_trapezium(1, float('inf'), 2), 3.0)
        self.assertEqual(median_trapezium(1, 1, float('inf')), 1.0)
        self.assertEqual(median_trapezium(-1, 1, 2), -0.5)
        self.assertEqual(median_trapezium(1, -1, 2), 0.5)
        self.assertEqual(median_trapezium(1, 1, -1), 1.0)
