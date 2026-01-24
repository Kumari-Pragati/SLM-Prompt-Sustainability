import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 1), [4, 5, 1, 2, 3])

    def test_boundary_conditions(self):
        self.assertEqual(rotate_right([], 0, 0), [])
        self.assertEqual(rotate_right([1], 0, 0), [1])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 0, 0), [1, 2, 3, 4, 5])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 5, 0), [1, 2, 3, 4, 5])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 0, 5), [1, 2, 3, 4, 5])

    def test_edge_cases(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 3, 2), [3, 4, 1, 2, 5])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 3), [2, 3, 4, 5, 1])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 1, 1), [2, 3, 4, 5, 1])
