import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(median_trapezium(3, 4, 5), 3.5)

    def test_edge_cases(self):
        self.assertEqual(median_trapezium(0, 0, 0), 0)
        self.assertEqual(median_trapezium(1, 1, 1), 1)
        self.assertEqual(median_trapezium(2, 2, 2), 2)

    def test_negative_inputs(self):
        self.assertEqual(median_trapezium(-1, -2, 3), -0.5)
        self.assertEqual(median_trapezium(-3, -4, 5), -1.5)

    def test_zero_height(self):
        self.assertEqual(median_trapezium(1, 2, 0), 1.5)

    def test_zero_base(self):
        self.assertEqual(median_trapezium(0, 0, 3), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            median_trapezium('a', 'b', 3)
        with self.assertRaises(TypeError):
            median_trapezium(1, 'b', 3)
        with self.assertRaises(TypeError):
            median_trapezium(1, 2, 'c')
