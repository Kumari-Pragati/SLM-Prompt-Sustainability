import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2, 3), [3, 4, 5, 1, 2])
        self.assertEqual(rotate_right([1, 2, 3], 1, 1), [3, 1, 2])
        self.assertEqual(rotate_right([1], 1, 1), [1])

    def test_edge_cases(self):
        self.assertEqual(rotate_right([1, 2, 3], 0, 1), [3, 1, 2])
        self.assertEqual(rotate_right([1, 2, 3], 4, 0), [1, 2, 3])
        self.assertEqual(rotate_right([], 2, 3), [])

    def test_complex(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5, 6], 3, 2), [4, 5, 6, 1, 2, 3])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5, 6], 1, 0), [2, 3, 4, 5, 6, 1])
        self.assertEqual(rotate_right([1, 2, 3, 4, 5, 6], 5, 0), [1, 2, 3, 4, 6, 5])
