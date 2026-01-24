import unittest
from mbpp_328_code import rotate_left

class TestRotateLeft(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 2, 3), [3, 4, 5, 1, 2])

    def test_boundary_conditions(self):
        self.assertEqual(rotate_left([], 0, 0), [])
        self.assertEqual(rotate_left([1], 0, 1), [1])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 0, 0), [1, 2, 3, 4, 5])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 5, 0), [1, 2, 3, 4, 5])

    def test_edge_cases(self):
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 1, 5), [5, 1, 2, 3, 4])
        self.assertEqual(rotate_left([1, 2, 3, 4, 5], 3, 2), [4, 5, 1, 2, 3])
