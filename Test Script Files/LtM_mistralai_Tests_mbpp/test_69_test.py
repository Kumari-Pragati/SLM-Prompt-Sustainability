import unittest
from mbpp_69_code import is_sublist

class TestIsSublist(unittest.TestCase):

    def test_empty_sublist(self):
        self.assertTrue(is_sublist([], []))

    def test_equal_lists(self):
        self.assertTrue(is_sublist([1, 2, 3], [1, 2, 3]))
        self.assertTrue(is_sublist([3, 2, 1], [1, 2, 3]))

    def test_sublist_longer_than_list(self):
        self.assertFalse(is_sublist([1, 2, 3], [1, 2, 3, 4]))

    def test_sublist_shorter_than_list(self):
        self.assertTrue(is_sublist([1, 2, 3], [1, 2, 3, 4, 5]))
        self.assertTrue(is_sublist([1, 2], [1, 2, 3, 4]))

    def test_sublist_with_duplicates(self):
        self.assertTrue(is_sublist([1, 2, 2, 3], [2, 2, 3]))

    def test_sublist_with_different_order(self):
        self.assertTrue(is_sublist([1, 2, 3], [3, 1, 2]))

    def test_sublist_with_non_matching_elements(self):
        self.assertFalse(is_sublist([1, 2, 3], [1, 2, 4]))
        self.assertFalse(is_sublist([1, 2, 3], [3, 2, 5]))
