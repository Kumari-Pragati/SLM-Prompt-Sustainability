import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):

    def test_valid_input(self):
        self.assertAlmostEqual(largest_triangle(5, 10), 12.5)

    def test_zero_input(self):
        with self.assertRaises(ValueError):
            largest_triangle(0, 10)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            largest_triangle(-5, 10)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            largest_triangle('a', 10)

    def test_edge_case(self):
        self.assertAlmostEqual(largest_triangle(0.1, 0.1), 0.1)

    def test_edge_case2(self):
        self.assertAlmostEqual(largest_triangle(10, 10), 10)
