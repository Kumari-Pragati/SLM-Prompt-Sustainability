import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(largest_triangle(10, 2), 150.0, places=1)

    def test_edge_case(self):
        self.assertEqual(largest_triangle(0, 2), -1)
        self.assertEqual(largest_triangle(10, 0), -1)
        self.assertEqual(largest_triangle(-10, 2), -1)
        self.assertEqual(largest_triangle(10, -2), -1)

    def test_boundary_case(self):
        self.assertAlmostEqual(largest_triangle(1, 1), 0.8660254037844386)
        self.assertAlmostEqual(largest_triangle(100, 1), 2474.873734152904)
