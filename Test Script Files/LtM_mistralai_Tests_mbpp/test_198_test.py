import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):

    def test_simple_positive_inputs(self):
        self.assertAlmostEqual(largest_triangle(3, 4), 2.598076211353776)
        self.assertAlmostEqual(largest_triangle(4, 5), 3.0)
        self.assertAlmostEqual(largest_triangle(5, 6), 3.330669073875856)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(largest_triangle(0, 1), -1)
        self.assertAlmostEqual(largest_triangle(1e-6, 1), 0)
        self.assertAlmostEqual(largest_triangle(1, 1e-6), -1)
        self.assertAlmostEqual(largest_triangle(1, 1), 0.4330127018922193)

    def test_negative_inputs(self):
        self.assertEqual(largest_triangle(-1, 1), -1)
        self.assertEqual(largest_triangle(1, -1), -1)
