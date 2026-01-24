import unittest
from mbpp_69_code import is_sublist

class TestIsSublist(unittest.TestCase):

    def test_empty_list(self):
        self.assertTrue(is_sublist([], []))
        self.assertTrue(is_sublist([], [1, 2, 3]))
        self.assertFalse(is_sublist([], [4, 5]) )

    def test_single_element_lists(self):
        self.assertFalse(is_sublist([1], []))
        self.assertTrue(is_sublist([], [1]))
        self.assertTrue(is_sublist([1], [1]))
        self.assertFalse(is_sublist([2], [1]))

    def test_equal_lists(self):
        self.assertTrue(is_sublist([1, 2, 3], [1, 2, 3]))
        self.assertTrue(is_sublist([3, 2, 1], [1, 2, 3]))
        self.assertTrue(is_sublist([1, 2, 3], [1, 2, 3, 4]))

    def test_sublists(self):
        self.assertTrue(is_sublist([1, 2, 3], [1, 2]))
        self.assertTrue(is_sublist([1, 2, 3, 4], [1, 2, 3]))
        self.assertFalse(is_sublist([1, 2, 3], [1, 2, 4]))
        self.assertFalse(is_sublist([1, 2, 3], [2, 1, 3]))

    def test_longer_list(self):
        self.assertFalse(is_sublist([1, 2, 3], [1, 2, 3, 4, 5]))
