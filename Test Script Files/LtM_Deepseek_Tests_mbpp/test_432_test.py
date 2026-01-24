import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(median_trapezium(10, 20, 5), 15)
        self.assertEqual(median_trapezium(3, 7, 2), 5)

    def test_edge_conditions(self):
        self.assertEqual(median_trapezium(0, 0, 0), 0)
        self.assertEqual(median_trapezium(100, 100, 100), 100)
        self.assertEqual(median_trapezium(-10, -20, -5), -15)

    def test_boundary_conditions(self):
        self.assertEqual(median_trapezium(float('inf'), float('inf'), 10), float('inf'))
        self.assertEqual(median_trapezium(-float('inf'), -float('inf'), -10), -float('inf'))

    def test_complex_cases(self):
        self.assertEqual(median_trapezium(1000000000, 2000000000, 500000000), 1500000000)
        self.assertEqual(median_trapezium(0.1, 0.2, 0.1), 0.15)
