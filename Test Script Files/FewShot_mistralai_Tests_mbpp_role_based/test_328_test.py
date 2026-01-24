import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 3), [3, 4, 5, 1, 2])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 3), [3, 4, 5, 1, 2])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 4, 5), [1, 2, 3, 4])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(rotate_left([], 0, 0), [])
        self.assertEqual(rotate_left([1], 0, 0), [1])
        self.assertEqual(rotate_left([1], 1, 1), [1])
        self.assertEqual(rotate_left([1, 2], 0, 1), [2])
        self.assertEqual(rotate_left([1, 2], 1, 0), [2])
        self.assertEqual(rotate_left([1, 2], 2, 0), [2, 1])
        self.assertEqual(rotate_left([1, 2], 1, 2), [2])
        self.assertEqual(rotate_left([1, 2], 2, 2), [1])

    def test_invalid_inputs(self):
        self.assertRaises(IndexError, rotate_left, [1, 2], -1, 1)
        self.assertRaises(IndexError, rotate_left, [1, 2], 1, -1)
        self.assertRaises(IndexError, rotate_left, [1, 2], len([1, 2]), 1)
        self.assertRaises(IndexError, rotate_left, [1, 2], 1, len([1, 2]))
