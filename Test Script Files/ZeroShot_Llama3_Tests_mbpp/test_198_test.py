import unittest
from mbpp_198_code import largest_triangle

class TestLargestTriangle(unittest.TestCase):

    def test_largest_triangle_valid_input(self):
        self.assertAlmostEqual(largest_triangle(1, 2), 0.8660254037844386)
        self.assertAlmostEqual(largest_triangle(2, 3), 2.598076211353316)
        self.assertAlmostEqual(largest_triangle(3, 4), 4.330127018922193)

    def test_largest_triangle_invalid_input(self):
        self.assertEqual(largest_triangle(-1, 2), -1)
        self.assertEqual(largest_triangle(1, -2), -1)
        self.assertEqual(largest_triangle(-1, -2), -1)

    def test_largest_triangle_zero_input(self):
        self.assertEqual(largest_triangle(0, 0), -1)
        self.assertEqual(largest_triangle(0, 1), -1)
        self.assertEqual(largest_triangle(1, 0), -1)
