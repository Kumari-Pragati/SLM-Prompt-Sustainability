import unittest
from mbpp_449_code import check_Triangle

class TestCheckTriangle(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(check_Triangle(3, 4, 4, 6, 6, 8), 'Yes')
        self.assertEqual(check_Triangle(-3, -4, -4, -6, -6, -8), 'Yes')
        self.assertEqual(check_Triangle(0, 0, 0, 0, 0, 0), 'Yes')

    def test_edge_cases(self):
        self.assertEqual(check_Triangle(0, 0, 0, 1, 0, 1), 'Yes')
        self.assertEqual(check_Triangle(0, 0, 1, 0, 0, 1), 'Yes')
        self.assertEqual(check_Triangle(1, 1, 1, 1, 1, 1), 'No')
        self.assertEqual(check_Triangle(1, 1, 2, 2, 3, 3), 'Yes')
        self.assertEqual(check_Triangle(-1, -1, -2, -2, -3, -3), 'Yes')

    def test_invalid_inputs(self):
        self.assertRaises(ValueError, check_Triangle, 0, 0, 0, 'x', 0, 0)
        self.assertRaises(ValueError, check_Triangle, 0, 0, 'x', 0, 0, 0)
        self.assertRaises(ValueError, check_Triangle, 0, 'y', 0, 0, 0, 0)
        self.assertRaises(ValueError, check_Triangle, 'x', 0, 0, 0, 0, 0)
