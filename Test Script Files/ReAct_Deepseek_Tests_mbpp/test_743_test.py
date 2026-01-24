import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 1), [4, 5, 1, 2, 3])

    def test_boundary_case(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 0, 0), [1, 2, 3, 4, 5])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 5, 5), [])

    def test_edge_case(self):
        self.assertEqual(rotate_right([], 2, 1), [])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 6, 0), [2, 3, 4, 5, 1])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 0, 6), [5, 1, 2, 3, 4])
