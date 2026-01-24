import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(median_trapezium(10, 20, 5), 15)

    def test_boundary_conditions(self):
        self.assertEqual(median_trapezium(0, 0, 0), 0)
        self.assertEqual(median_trapezium(1000000000, 1000000000, 1000000000), 1000000000)

    def test_edge_conditions(self):
        self.assertEqual(median_trapezium(1, 2, 1), 1.5)
        self.assertEqual(median_trapezium(1, 1, 1), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            median_trapezium("10", 20, 5)
        with self.assertRaises(TypeError):
            median_trapezium(10, "20", 5)
        with self.assertRaises(TypeError):
            median_trapezium(10, 20, "5")
