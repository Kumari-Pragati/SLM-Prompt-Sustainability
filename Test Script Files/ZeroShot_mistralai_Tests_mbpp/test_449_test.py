import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):

    def test_degenerate_triangle(self):
        self.assertEqual(check_Triangle(0, 0, 0, 0, 0, 0), 'No')
        self.assertEqual(check_Triangle(0, 0, 0, 0, 1, 0), 'No')
        self.assertEqual(check_Triangle(0, 0, 0, 1, 0, 0), 'No')

    def test_collinear_triangle(self):
        self.assertEqual(check_Triangle(0, 0, 1, 0, 2, 0), 'No')
        self.assertEqual(check_Triangle(0, 0, 1, 1, 2, 2), 'No')
        self.assertEqual(check_Triangle(0, 1, 1, 0, 1, 1), 'No')

    def test_valid_triangle(self):
        self.assertEqual(check_Triangle(0, 0, 1, 1, 1, 1), 'Yes')
        self.assertEqual(check_Triangle(0, 0, 1, 0, 1, 1), 'Yes')
        self.assertEqual(check_Triangle(1, 0, 1, 1, 0, 1), 'Yes')

    def test_invalid_triangle(self):
        self.assertEqual(check_Triangle(0, 0, 1, 1, 2, 2), 'No')
        self.assertEqual(check_Triangle(1, 0, 1, 1, 2, 3), 'No')
        self.assertEqual(check_Triangle(1, 1, 1, 1, 2, 2), 'No')
