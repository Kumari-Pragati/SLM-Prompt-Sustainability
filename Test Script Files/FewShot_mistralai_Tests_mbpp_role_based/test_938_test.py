import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(find_closet([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], 3, 4, 4), (1, 5, 9))
        self.assertEqual(find_closet([-1, 0, 1], [-2, -1, 0], [-3, -2, -1], 3, 3, 3), (-1, -2, -3))
        self.assertEqual(find_closet([0, 1, 2], [3, 2, 1], [0, 1, 2], 3, 3, 3), (0, 3, 0))

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_closet([], [], [], 0, 0, 0), (None, None, None))
        self.assertEqual(find_closet([1], [], [], 1, 0, 0), (1, None, None))
        self.assertEqual(find_closet([], [1], [], 0, 1, 0), (None, 1, None))
        self.assertEqual(find_closet([1], [1], [], 1, 1, 0), (1, 1, None))
        self.assertEqual(find_closet([1], [1], [1], 1, 1, 1), (1, 1, 1))
        self.assertEqual(find_closet([1, 2], [1, 2], [1, 2], 2, 2, 2), (1, 1, 1))
