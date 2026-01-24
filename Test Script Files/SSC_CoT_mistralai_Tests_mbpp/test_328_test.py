import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 3), [3, 4, 5, 1, 2])
        self.assertEqual(rotate_left(['a', 'b', 'c', 'd', 'e'], 2, 3), ['c', 'd', 'e', 'a', 'b'])

    def test_edge_cases(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 3), [3, 4, 5, 1, 2])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 4, 3), [3, 4, 5, 1, 2])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 0), [1, 2, 3, 4, 5])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 6), [3, 4, 5, 1, 2])

    def test_boundary_cases(self):
        self.assertEqual(rotate_left([1], 0, 1), [1])
        self.assertEqual(rotate_left([1], 1, 0), [1])
        self.assertEqual(rotate_left([1], 1, 1), [1])

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            rotate_left([1], -1, 1)
        with self.assertRaises(ValueError):
            rotate_left([1], 1, -1)
        with self.assertRaises(ValueError):
            rotate_left([1], len([1]), 1)
        with self.assertRaises(ValueError):
            rotate_left([1], 1, len([1]))
