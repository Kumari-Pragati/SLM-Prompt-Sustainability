import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 3), [3, 4, 5, 1, 2])

    def test_boundary_conditions(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 0), [1, 2, 3, 4, 5])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 5, 5), [])

    def test_edge_conditions(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 1, 5), [5, 1, 2, 3, 4])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 5, 1), [2, 3, 4, 5, 1])

    def test_invalid_inputs(self):
        with self.assertRaises(IndexError):
            rotate_left([1, 2, 3, 4, 5], 6, 3)
        with self.assertRaises(IndexError):
            rotate_left([1, 2, 3, 4, 5], 3, 6)
