import unittest
from mbpp_846_code import find_platform

class TestFindPlatform(unittest.TestCase):

    def test_empty_arrays(self):
        self.assertEqual(find_platform([], [], 0), 0)
        self.assertEqual(find_platform([], [1], 1), 0)
        self.assertEqual(find_platform([1], [], 1), 1)

    def test_single_element_arrays(self):
        self.assertEqual(find_platform([1], [1], 1), 1)
        self.assertEqual(find_platform([2], [1], 1), 0)
        self.assertEqual(find_platform([1], [2], 1), 0)

    def test_equal_arrays(self):
        self.assertEqual(find_platform([1, 1, 1], [1, 1, 1], 3), 3)

    def test_different_arrays(self):
        self.assertEqual(find_platform([1, 2, 3], [2, 3, 4], 3), 1)
        self.assertEqual(find_platform([1, 2, 3], [3, 2, 1], 3), 1)
        self.assertEqual(find_platform([3, 2, 1], [1, 2, 3], 3), -1)

    def test_sorted_arrays(self):
        self.assertEqual(find_platform([1, 2, 3], [2, 3, 4], 3), 1)
        self.assertEqual(find_platform([3, 2, 1], [1, 2, 3], 3), 1)
        self.assertEqual(find_platform([3, 2, 1], [3, 2, 1], 3), 3)

    def test_negative_n(self):
        self.assertRaises(ValueError, find_platform, [1, 2, 3], [2, 3, 4], -1)

    def test_empty_dep(self):
        self.assertRaises(IndexError, find_platform, [1, 2, 3], [], 3)

    def test_empty_arr(self):
        self.assertRaises(IndexError, find_platform, [], [1, 2, 3], 3)
