import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):

    def test_valid_triangle(self):
        # Typical case: valid triangle with positive coordinates
        self.assertEqual(check_Triangle(0, 0, 1, 1, 1, 0), 'Yes')
        self.assertEqual(check_Triangle(-1, -1, 1, 1, 0, 0), 'Yes')
        self.assertEqual(check_Triangle(0, 0, 0, 1, 1, 1), 'Yes')

    def test_degenerate_triangle(self):
        # Edge case: degenerate triangle (collinear points)
        self.assertEqual(check_Triangle(0, 0, 0, 0, 1, 1), 'No')
        self.assertEqual(check_Triangle(0, 0, 1, 0, 1, 0), 'No')
        self.assertEqual(check_Triangle(1, 1, 1, 0, 0, 0), 'No')

    def test_invalid_triangle(self):
        # Edge case: invalid triangle (one side is zero length)
        self.assertEqual(check_Triangle(0, 0, 0, 1, 0, 0), 'No')
        self.assertEqual(check_Triangle(0, 1, 1, 0, 0, 0), 'No')
        self.assertEqual(check_Triangle(1, 0, 0, 0, 0, 1), 'No')

    def test_negative_coordinates(self):
        # Edge case: negative coordinates
        self.assertEqual(check_Triangle(-1, -1, -1, -1, -1, -1), 'Yes')
        self.assertEqual(check_Triangle(-1, -1, 1, -1, -1, -1), 'No')
        self.assertEqual(check_Triangle(1, -1, -1, -1, 1, -1), 'No')

    def test_zero_coordinates(self):
        # Edge case: zero coordinates
        self.assertEqual(check_Triangle(0, 0, 0, 0, 0, 0), 'No')
