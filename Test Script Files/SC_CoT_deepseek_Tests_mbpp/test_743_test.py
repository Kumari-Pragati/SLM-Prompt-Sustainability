import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 3), [3, 4, 1, 2])

    def test_boundary_case(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 0, 0), [1, 2, 3, 4, 5])

    def test_edge_case(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 5, 5), [])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 5, 0), [1, 2, 3, 4, 5])

    def test_special_case(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 3, 2), [4, 5, 1, 2, 3])

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            rotate_right([1, 2, 3, 4, 5], 6, 3)
        with self.assertRaises(IndexError):
            rotate_right([1, 2, 3, 4, 5], 3, 6)
