import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):

    def test_empty_lists(self):
        self.assertEqual(find_closet([], [], [], 0, 0, 0), (sys.maxsize, sys.maxsize, sys.maxsize))
        self.assertEqual(find_closet([], [1], [], 0, 1, 0), (sys.maxsize, 1, sys.maxsize))
        self.assertEqual(find_closet([1], [], [2], 1, 0, 1), (1, sys.maxsize, 2))
        self.assertEqual(find_closet([1], [2], [], 1, 0, 1), (1, 2, sys.maxsize))
        self.assertEqual(find_closet([], [1], [2], 0, 1, 1), (sys.maxsize, 1, 2))

    def test_single_element_lists(self):
        self.assertEqual(find_closet([1], [2], [3], 1, 1, 1), (1, 2, 3))
        self.assertEqual(find_closet([1], [1], [2], 1, 1, 1), (1, 1, 2))
        self.assertEqual(find_closet([1], [2], [1], 1, 1, 1), (1, 2, 1))

    def test_equal_lists(self):
        self.assertEqual(find_closet([1, 2, 3], [1, 2, 3], [1, 2, 3], 3, 3, 3), (1, 2, 3))
        self.assertEqual(find_closet([1, 2, 3], [1, 2, 3], [1, 2, 4], 3, 3, 4), (1, 2, 4))
        self.assertEqual(find_closet([1, 2, 3], [1, 2, 3], [1, 4, 3], 3, 3, 4), (1, 2, 3))

    def test_lists_with_duplicates(self):
        self.assertEqual(find_closet([1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 3], 4, 4, 4), (1, 2, 3))
        self.assertEqual(find_closet([1, 1, 2, 3], [1, 2, 2, 3], [1, 2, 3, 4], 4, 4, 4), (1, 2, 4))
        self.assertEqual(find_closet([1, 1, 2, 3], [1, 2, 2, 3], [1, 4, 3, 3], 4, 4, 4), (1, 2, 3))

    def test_lists_with_no_closest(self):
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, 9], 3, 3, 3), (sys.maxsize, sys.maxsize, sys.maxsize))
        self.assertEqual(find_closet([1, 2, 3], [4, 5, 6], [7, 8, sys.maxsize], 3, 3, sys.maxsize // 2), (1, 2, sys.maxsize))
        self.assertEqual(find_closet([1, 2, sys.maxsize], [4, 5, 6], [7, 8, 9], sys.maxsize // 2, 3, 3), (1, 2, 3))
