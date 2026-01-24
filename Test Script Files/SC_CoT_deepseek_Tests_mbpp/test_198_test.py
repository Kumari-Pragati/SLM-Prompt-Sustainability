import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(largest_triangle(10, 2), 15.588457268119896)

    def test_boundary_case(self):
        self.assertEqual(largest_triangle(0, 2), -1)
        self.assertEqual(largest_triangle(10, 0), -1)
        self.assertEqual(largest_triangle(-10, 2), -1)
        self.assertEqual(largest_triangle(10, -2), -1)

    def test_edge_case(self):
        self.assertAlmostEqual(largest_triangle(1, 1), 1.369306392681208)
        self.assertAlmostEqual(largest_triangle(100, 100), 3464.101615137754)

    def test_invalid_input(self):
        self.assertEqual(largest_triangle(-10, -2), -1)
        self.assertEqual(largest_triangle('a', 2), -1)
        self.assertEqual(largest_triangle(10, 'b'), -1)
        self.assertEqual(largest_triangle('a', 'b'), -1)
