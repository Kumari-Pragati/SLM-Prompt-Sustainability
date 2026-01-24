import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 3), [3, 4, 5, 1, 2])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 3), [3, 4, 5, 1, 2])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 4, 2), [5, 1, 2])

    def test_edge_case(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 0), [])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 5, 0), [1, 2, 3, 4, 5])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], -1, 2), [3, 4, 5, 1, 2])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, -1), [1, 2, 3, 4, 5])

    def test_corner_case(self):
        self.assertEqual(rotate_left([], 2, 3), [])
        self.assertEqual(rotate_left([1], 2, 3), [1])
        self.assertEqual(rotate_left([1, 2], 0, 0), [2])
        self.assertEqual(rotate_left([1, 2], 1, 0), [2])
        self.assertEqual(rotate_left([1, 2], 2, 0), [1])
