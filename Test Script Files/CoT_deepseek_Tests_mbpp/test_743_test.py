import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 1), [4, 5, 1, 2, 3])

    def test_boundary_conditions(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 0, 0), [1, 2, 3, 4, 5])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 5, 0), [2, 3, 4, 5, 1])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 0, 5), [5, 1, 2, 3, 4])

    def test_edge_cases(self):
        self.assertEqual(rotate_right([], 2, 1), [])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 6, 0), [2, 3, 4, 5, 1])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 0, 6), [5, 1, 2, 3, 4])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], -2, 1), [3, 4, 5, 1, 2])

    def test_invalid_inputs(self):
        with self.assertRaises(IndexError):
            rotate_right([1, 2, 3, 4, 5], 6, 0)
        with self.assertRaises(IndexError):
            rotate_right([1, 2, 3, 4, 5], 0, 6)
