import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):

    def test_simple_triangle(self):
        self.assertEqual(check_Triangle(0, 0, 1, 1, 1, 0), 'Yes')
        self.assertEqual(check_Triangle(1, 1, 2, 2, 3, 3), 'Yes')
        self.assertEqual(check_Triangle(-1, -1, 0, 0, 1, 1), 'Yes')

    def test_edge_and_boundary(self):
        self.assertEqual(check_Triangle(0, 0, 1, 0, 1, 0), 'Yes')
        self.assertEqual(check_Triangle(1, 0, 1, 1, 0, 0), 'Yes')
        self.assertEqual(check_Triangle(1, 1, 0, 0, 0, 0), 'No')
        self.assertEqual(check_Triangle(1, 1, 2, 2, 3, 4), 'Yes')
        self.assertEqual(check_Triangle(-1, -1, 0, 0, 1, 1), 'Yes')
        self.assertEqual(check_Triangle(0, 0, 1, 1, -1, -1), 'Yes')

    def test_degenerate_cases(self):
        self.assertEqual(check_Triangle(0, 0, 0, 0, 0, 0), 'No')
        self.assertEqual(check_Triangle(1, 1, 1, 1, 1, 1), 'No')
        self.assertEqual(check_Triangle(1, 1, 1, 1, -1, -1), 'No')

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, check_Triangle, 0, 0, 0, 0, 'a', 'b')
        self.assertRaises(ValueError, check_Triangle, -1, -1, 0, 0, 0, 0)
