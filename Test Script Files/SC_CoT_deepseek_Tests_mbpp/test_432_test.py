import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(median_trapezium(10, 20, 5), 15)

    def test_boundary_case(self):
        self.assertAlmostEqual(median_trapezium(0, 0, 0), 0)

    def test_edge_case(self):
        self.assertAlmostEqual(median_trapezium(1000000000, 2000000000, 1), 1500000000)

    def test_special_case(self):
        self.assertAlmostEqual(median_trapezium(1, 1, 1), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            median_trapezium("10", 20, 5)
