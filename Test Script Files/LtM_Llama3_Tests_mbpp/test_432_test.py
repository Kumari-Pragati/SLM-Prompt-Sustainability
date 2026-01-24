import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(median_trapezium(1, 2, 3), 1.5)
        self.assertEqual(median_trapezium(4, 5, 6), 4.5)
        self.assertEqual(median_trapezium(7, 8, 9), 7.5)

    def test_edge_cases(self):
        self.assertEqual(median_trapezium(0, 0, 0), 0)
        self.assertEqual(median_trapezium(1, 1, 1), 1)
        self.assertEqual(median_trapezium(10, 10, 10), 10)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            median_trapezium('a', 'b', 'c')
        with self.assertRaises(TypeError):
            median_trapezium(1, 'b', 3)
        with self.assertRaises(TypeError):
            median_trapezium(1, 2, 'c')
