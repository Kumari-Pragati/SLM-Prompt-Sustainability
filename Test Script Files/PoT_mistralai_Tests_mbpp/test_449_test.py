import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(check_Triangle(0, 0, 1, 1, 1, 0), 'Yes')
        self.assertEqual(check_Triangle(0, 0, -1, -1, 1, 1), 'Yes')
        self.assertEqual(check_Triangle(3, 4, 5, 6, 7, 8), 'Yes')

    def test_edge_cases(self):
        self.assertEqual(check_Triangle(0, 0, 0, 0, 1, 1), 'Yes')
        self.assertEqual(check_Triangle(0, 0, 1, 0, 0, 1), 'Yes')
        self.assertEqual(check_Triangle(0, 0, -1, 0, 0, 1), 'No')
        self.assertEqual(check_Triangle(0, 0, 0, 1, 0, 0), 'No')

    def test_boundary_cases(self):
        self.assertEqual(check_Triangle(-1, -1, 0, 0, 1, 1), 'Yes')
        self.assertEqual(check_Triangle(0, 0, 1, 1, 0, 0), 'Yes')
        self.assertEqual(check_Triangle(1, 1, 0, 0, -1, -1), 'Yes')
        self.assertEqual(check_Triangle(0, 0, 1, 1, 1, 0), 'Yes')
        self.assertEqual(check_Triangle(-1, -1, -1, -1, 0, 0), 'No')
        self.assertEqual(check_Triangle(1, 1, 1, 1, 0, 0), 'No')
