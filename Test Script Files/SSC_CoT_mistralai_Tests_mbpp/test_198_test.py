import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):
    def test_normal_input(self):
        self.assertAlmostEqual(largest_triangle(3, 4), 2.5980762113537757)
        self.assertAlmostEqual(largest_triangle(4, 3), 2.5980762113537757)
        self.assertAlmostEqual(largest_triangle(5, 12), 6.0)

    def test_edge_input(self):
        self.assertEqual(largest_triangle(0, 4), -1)
        self.assertEqual(largest_triangle(3, 0), -1)
        self.assertEqual(largest_triangle(-3, 4), -1)
        self.assertEqual(largest_triangle(3, -4), -1)

    def test_boundary_input(self):
        self.assertAlmostEqual(largest_triangle(1, 1), 1.7320508075688772)
        self.assertAlmostEqual(largest_triangle(1, 2), 2.5980762113537757)
        self.assertAlmostEqual(largest_triangle(2, 1), 2.5980762113537757)
