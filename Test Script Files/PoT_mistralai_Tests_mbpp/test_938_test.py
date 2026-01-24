import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_closet([1, 2, 3, 4], [5, 6, 7], [8, 9, 10], 3, 3, 3), (1, 5, 8))
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 3, 3, 3), (1, 4, 7))
        self.assertEqual(find_closet([1, 2, 3], [1, 2, 3], [4, 5, 6], 3, 3, 3), (1, 1, 4))

    def test_edge_case_empty_lists(self):
        self.assertEqual(find_closet([], [], [], 0, 0, 0), (None, None, None))
        self.assertEqual(find_closet([1], [], [], 1, 0, 0), (1, None, None))
        self.assertEqual(find_closet([], [1], [], 0, 1, 0), (None, 1, None))
        self.assertEqual(find_closet([1], [1], [], 1, 1, 0), (1, 1, None))

    def test_edge_case_single_element(self):
        self.assertEqual(find_closet([1], [2], [3], 1, 1, 1), (1, 2, 3))
        self.assertEqual(find_closet([1], [1], [2], 1, 1, 1), (1, 1, 2))
        self.assertEqual(find_closet([1], [1], [1], 1, 1, 1), (1, 1, 1))

    def test_edge_case_different_list_lengths(self):
        self.assertEqual(find_closet([1, 2], [3], [4], 2, 1, 1), (1, 3, 4))
        self.assertEqual(find_closet([1, 2], [1, 3], [], 2, 2, 0), (1, 1, None))
        self.assertEqual(find_closet([1, 2], [1, 3], [4], 2, 2, 1), (1, 1, 4))
