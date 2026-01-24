import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(largest_triangle(3, 4), 2.67949)
        self.assertAlmostEqual(largest_triangle(4, 3), 2.67949)

    def test_edge_case_a(self):
        self.assertEqual(largest_triangle(0, 4), -1)
        self.assertEqual(largest_triangle(3, 0), -1)

    def test_edge_case_b(self):
        self.assertEqual(largest_triangle(1, 1), 1.73205)

    def test_corner_case(self):
        self.assertAlmostEqual(largest_triangle(1, 1e-6), 1.73205)
        self.assertAlmostEqual(largest_triangle(1e-6, 1), 1.73205)
