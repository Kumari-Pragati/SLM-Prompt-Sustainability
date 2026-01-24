import unittest
from mbpp_938_code import find_closet

class TestFindCloset(unittest.TestCase):

    def test_find_closet_positive(self):
        self.assertEqual(find_closet([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], 4, 4, 4), (1, 5, 9))
        self.assertEqual(find_closet([-1, 0, 1, 2], [-3, -2, -1, 0], [-4, -3, -2, -1], 4, 4, 4), (0, -3, -4))
        self.assertEqual(find_closet([0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], 3, 3, 3), (0, 4, 8))

    def test_find_closet_empty_lists(self):
        self.assertEqual(find_closet([], [], [], 0, 0, 0), (None, None, None))
        self.assertEqual(find_closet([], [1], [], 1, 1, 0), (None, 1, None))
        self.assertEqual(find_closet([1], [], [2], 1, 0, 1), (1, None, 2))
        self.assertEqual(find_closet([], [1], [2], 0, 1, 1), (None, 1, 2))

    def test_find_closet_single_elements(self):
        self.assertEqual(find_closet([1], [2], [3], 1, 1, 1), (1, 2, 3))
        self.assertEqual(find_closet([2], [1], [3], 1, 1, 1), (2, 1, 3))
        self.assertEqual(find_closet([3], [1], [2], 1, 1, 1), (3, 1, 2))

    def test_find_closet_invalid_inputs(self):
        self.assertRaises(TypeError, find_closet, [1], [2], [3], 'a', 'b', 'c')
        self.assertRaises(TypeError, find_closet, [1], [2], [3], 1, 'b', 'c')
        self.assertRaises(TypeError, find_closet, [1], [2], [3], 1, 1, 'c')
