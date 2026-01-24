import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 3), [3, 4, 5, 1, 2])
        self.assertEqual(rotate_left([0, 1, 2], 1, 2), [2, 0, 1])
        self.assertEqual(rotate_left([10, 20, 30], 1, 2), [30, 10, 20])

    def test_edge_cases(self):
        self.assertEqual(rotate_left([1, 2], 0, 1), [2])
        self.assertEqual(rotate_left([1, 2], 1, 0), [1])
        self.assertEqual(rotate_left([1, 2], 0, 0), [])
        self.assertEqual(rotate_left([1, 2], len([1, 2]), 1), [1])
        self.assertEqual(rotate_left([1, 2], len([1, 2]), 0), [2])

    def test_complex(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5, 6], 3, 4), [4, 5, 6, 1, 2, 3])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5, 6], 0, 3), [3, 4, 5])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5, 6], len([1, 2, 3, 4, 5, 6]), 2), [4, 5, 6])
