import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertAlmostEqual(largest_triangle(1, 2), 0.8660254037844386)
        self.assertAlmostEqual(largest_triangle(5, 10), 0.7071067811865475)
        self.assertAlmostEqual(largest_triangle(10, 20), 0.35355339059327373)

    def test_negative_numbers(self):
        self.assertEqual(largest_triangle(-1, 2), -1)
        self.assertEqual(largest_triangle(1, -2), -1)
        self.assertEqual(largest_triangle(-1, -2), -1)

    def test_zero(self):
        self.assertEqual(largest_triangle(0, 2), 0)
        self.assertEqual(largest_triangle(1, 0), 0)
        self.assertEqual(largest_triangle(0, 0), 0)
