import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):
    def test_valid_triangle(self):
        self.assertEqual(check_Triangle(0, 0, 1, 1, 1, 0), 'Yes')
        self.assertEqual(check_Triangle(-1, -1, 1, 1, 0, 0), 'Yes')
        self.assertEqual(check_Triangle(0, 0, 0, 1, 1, 1), 'Yes')

    def test_degenerate_triangle(self):
        self.assertEqual(check_Triangle(0, 0, 0, 0, 1, 1), 'No')
        self.assertEqual(check_Triangle(0, 0, 1, 0, 1, 0), 'No')
        self.assertEqual(check_Triangle(1, 0, 1, 1, 0, 0), 'No')

    def test_invalid_inputs(self):
        self.assertIsNone(check_Triangle(0, 0, 0, 0, 0, 0))
        self.assertIsNone(check_Triangle(1, 'a', 1, 1, 1, 1))
        self.assertIsNone(check_Triangle(-1, 0, 0, 0, 0, 0))
