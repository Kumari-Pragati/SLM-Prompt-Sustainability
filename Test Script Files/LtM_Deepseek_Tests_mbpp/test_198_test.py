import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertAlmostEqual(largest_triangle(1, 1), 0.8660254037844386)
        self.assertAlmostEqual(largest_triangle(2, 2), 2.509178474673485)

    def test_edge_conditions(self):
        self.assertEqual(largest_triangle(0, 1), 0)
        self.assertEqual(largest_triangle(1, 0), 0)
        self.assertEqual(largest_triangle(0, 0), 0)
        self.assertEqual(largest_triangle(-1, 1), -1)
        self.assertEqual(largest_triangle(1, -1), -1)
        self.assertEqual(largest_triangle(-1, -1), -1)

    def test_complex_cases(self):
        self.assertAlmostEqual(largest_triangle(10, 1), 25.09178474673485)
        self.assertAlmostEqual(largest_triangle(1, 10), 0.8660254037844386)
        self.assertAlmostEqual(largest_triangle(10, 10), 25.09178474673485)
