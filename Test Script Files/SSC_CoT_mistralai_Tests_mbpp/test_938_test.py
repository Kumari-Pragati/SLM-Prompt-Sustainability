import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(find_closet([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], 3, 3, 3), (1, 5, 9))
        self.assertEqual(find_closet([5, 6, 7, 8], [1, 2, 3, 4], [9, 10, 11, 12], 3, 3, 3), (1, 5, 9))
        self.assertEqual(find_closet([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], 3, 3, 3), (1, 5, 9))

    def test_edge_case_small_lists(self):
        self.assertEqual(find_closet([1], [2], [3], 1, 1, 1), (1, 2, 3))
        self.assertEqual(find_closet([1], [2], [3], 1, 1, 1), (1, 2, 3))
        self.assertEqual(find_closet([1], [2], [3], 1, 1, 1), (1, 2, 3))

    def test_edge_case_empty_lists(self):
        self.assertIsNone(find_closet([], [], [], 0, 0, 0))
        self.assertIsNone(find_closet([], [], [], 0, 0, 0))
        self.assertIsNone(find_closet([], [], [], 0, 0, 0))

    def test_edge_case_single_element(self):
        self.assertEqual(find_closet([1], [], [], 1, 0, 0), (1, None, None))
        self.assertEqual(find_closet([], [2], [], 0, 1, 0), (None, 2, None))
        self.assertEqual(find_closet([], [], [3], 0, 0, 1), (None, None, 3))
