import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(median_trapezium(5, 7, 3), 6.0)

    def test_edge_cases(self):
        self.assertEqual(median_trapezium(0, 0, 3), 0.0)
        self.assertEqual(median_trapezium(10, 10, 3), 10.0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            median_trapezium('a', 7, 3)
        with self.assertRaises(TypeError):
            median_trapezium(5, 'b', 3)
        with self.assertRaises(TypeError):
            median_trapezium(5, 7, 'c')

    def test_boundary_conditions(self):
        self.assertEqual(median_trapezium(0, 0, 0), 0.0)
        self.assertEqual(median_trapezium(10, 10, 0), 0.0)
