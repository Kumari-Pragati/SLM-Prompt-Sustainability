import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 3), [3, 4, 5, 1, 2])

    def test_boundary_case(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 0), [1, 2, 3, 4, 5])

    def test_edge_case(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 5, 5), [])

    def test_invalid_input(self):
        with self.assertRaises(IndexError):
            rotate_left([1, 2, 3, 4, 5], 6, 3)
