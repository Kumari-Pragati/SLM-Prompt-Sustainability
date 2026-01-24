import unittest
from mbpp_432_code import median_trapezium

class TestMedianTrapezium(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(median_trapezium(10, 20, 5), 15)

    def test_edge_case_with_zero_height(self):
        self.assertAlmostEqual(median_trapezium(10, 20, 0), 15)

    def test_boundary_case_with_equal_bases(self):
        self.assertAlmostEqual(median_trapezium(20, 20, 5), 20)

    def test_invalid_input_with_negative_height(self):
        with self.assertRaises(Exception):
            median_trapezium(10, 20, -5)
